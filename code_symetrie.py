def buildlist(key, base):
    table = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    tablel = []
    for letter in key:
        if letter in tablel:
            pass
        else:
            tablel.append(letter)
    for letter in table:
        if letter in tablel:
            pass
        else:
            tablel.append(letter)
    return tablel
def findletter(lettervar, tablel):
    temptable = ""
    for letter in tablel:
        temptable = letter + temptable
    tableb = []
    for letter in temptable:
        tableb.append(letter)
    newletter = ""
    if lettervar == "VV":
        for letter in lettervar:
            pos = tablel.index(letter)
            newletter += tableb[pos]
    else:
        pos = tablel.index(lettervar)
        newletter = tableb[pos]
    return newletter
def translate(key, string, base):
    table = buildlist(key, base)
    newstring = ""
    for letter in string:
        if letter in table:
            letter = letter.replace("W", "VV") # ligne qui convertit "W" par "VV"
            newstring += findletter(letter, table)
        else:
            newstring += letter
    return newstring
print(translate("CLE", "TEXTE", "ABCDEFGHIJKLMNOPQRSTUVXYZ"))