#!/usr/bin/python
#include "Python.h"

chaName = raw_input("Enter the name for your new character\n")

f = open(chaName+".html", "w+")
#f.write(chaName+"\n")
print ("You have 20 attribute points to split between Str, Dex, Wis, Cha\nHow will you distribute your points?\n")
i = 20
while i > 0:
	print ("How many points for Str?")
	strength = int(input())
	if strength > i:
		print ("Cheater!\n")
	i -= strength
	print ("How many points for Dex?")
	dex = int(input())
	if dex > i:
		print ("Cheater!\n")
	i -= dex
	print ("How many points for Wis?")
	wis = int(input())
	if wis > i:
		print ("Cheater!\n")
	i -= wis
	print ("How many points for Cha?")
	charm = int(input())
	if charm > i:
		print ("Cheater!\n")
	i -= charm

var = {strength: "strength", dex: "dexterity", wis: "wisdom", charm: "charisma" }
favAttribute = var.get(max(strength,dex,wis,charm))
if favAttribute in ["strength"]:
	className = "warrior"
	charClass = "01.jpg"
if favAttribute in ["dexterity"]:
	className = "ranger"
	charClass = "02.jpg"
if favAttribute in ["wisdom"]:
	className = "wizard"
	charClass = "03.jpg"
if favAttribute in ["charisma"]:
	className = "bard"
	charClass = "04.jpg"

print ("Your favored attribute is ",var.get(max(strength,dex,wis,charm)))

f.write("""<!DOCTYPE html>
<html>
<head>
<style>
body {
	background-color: linen;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
tr:nth-child(even) {
  background-color: #dddddd;
}

tr:nth-child(odd) {
  background-color: #ffffff;
}

</style>
</head>
<body>

<h2>"""+chaName+", the "+className+"""</h2>

<table>
<tr>
<td width="20%"><img src="""'"'+charClass+'"'""" width="80%" height="10%"></td>
	<td align="left">
	<table>
  	<tr>
    	<th>Stat</th>
    	<th>Value</th>
  	</tr>
  	<tr>
    	<td>Strength</td>
    	<td>"""+str(strength)+"""</td>
  	</tr>
  	<tr>
    	<td>Dexterity</td>
    	<td>"""+str(dex)+"""</td>
  	</tr>
  	<tr>
    	<td>Wisdom</td>
    	<td>"""+str(wis)+"""</td>
  	</tr>
  	<tr>
    	<td>Charisma</td>
    	<td>"""+str(charm)+"""</td>
  	</tr>
	</table>

	</td>
	</tr>
	</table>

</body>
</html>
""")

f.close()