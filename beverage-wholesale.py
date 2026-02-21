ad = False

drink = input("Menu:\nCoffee  |  Tea\n\nWhat would you like to order? (Please use only the first letter.)\n")
if drink == "c" or "C":
    amount = input("How much?\n(Ordered in kg)\n")
elif drink == "t" or "T":
    amount = input("How much?\n(Ordered in boxes)\n")
else:
    print("Invalid input.\nYou should enter c/C or t/T.")
    exit()
if amount > 0 and drink == "c" or "C":
    bdiscount = 18.50 * amount
    udrink = "Coffee"
    unit = "kg"
    if amount > 25:
        adiscount = (0.1 * 18.50) * amount
        ad = True
elif amount > 0 and drink == "t" or "T":
    bdiscount = (0.45 * 20) * amount
    udrink = "Tea"
    unit = "boxes"
    if amount > 10:
        adiscount = (0.1 * (0.45 * 20)) * amount
        ad = True
elif amount <= 0:
    print("Input must be greater than 0.")
    exit()
else:
    print("Unknown error. Please enter a valid number greater than 0.")
    exit()
province = input("--------------------------------\n Province                GST\n-AB/BC-----------------------5%-\n--ON------------------------13%-\n--Others--------------------15%-")
if province == "ab" or "AB" or "aB" or "Ba" or "bc" or "BC" or "Bc" or "bC":
    GST = 0.05
elif province == "ON" or "on" or "On" or "oN":
    GST = 0.13
else:
    GST = 0.15
if ad == True:
    print("---------------------\n", udrink, "\n", amount, unit, "\n---------------------\nStandard Price:\n$", bdiscount,"\n---------------------\nBulk Discount Price:\n$", adiscount, "\n---------------------\nGST:", GST, "\nTotal:\n", adiscount * GST, "\n---------------------")
else:
    print("---------------------\n", udrink, "\n", amount, unit, "\n---------------------\nStandard Price:\n$", bdiscount,"\n---------------------\nGST:", GST, "\nTotal:\n", adiscount * GST, "\n---------------------\n\nThank you.")
exit()