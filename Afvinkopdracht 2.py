#1
personalinfo = ("Yorick Cleijsen \nSirtemalaan 16, Grave Noord-Brabant, 5361 JZ \n06-37384074 \nBio-Informatics")
print(personalinfo)

print("////////////////////////////////////////////////////////////////")

#2
predicted_sales = input("Enter predicted sales")
profit = float(predicted_sales) * float("0.23")
print(profit)

print("////////////////////////////////////////////////////////////////")

#4 
item1 = input("Enter prize of item 1")
item2 = input("Enter prize of item 2")
item3 = input("Enter prize of item 3")
item4 = input("Enter prize of item 4")
item5 = input("Enter prize of item 5")

Item1 = float(item1) * float(0.07)
Item2 = float(item2) * float(0.07)
Item3 = float(item3) * float(0.07)
Item4 = float(item4) * float(0.07)
Item5 = float(item5) * float(0.07)

subtotal = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
print("subtotal")
print(subtotal)
tax = float(Item1) + float(Item2) + float(Item3) + float(Item4) + float(Item5)
print("tax")
print(tax)

total = float(tax) + float(subtotal)
print("total")
print(total)

print("////////////////////////////////////////////////////////////////")

#5
speed = int(input("Enter you driving speed in miles per hour"))
time = int(input("Enter your estimated driving time"))
distance = speed * time
print(distance)

print("Distance travels after '6' hours")
milesI = float("70") * float("6")
print(milesI)

print("Distance travels after '10' hours")
milesII = float("70") * float("10")
print(milesII)

print("Distance travels after '15' hours")
milesIII = float("70") * float("15")
print(milesIII)

print("////////////////////////////////////////////////////////////////")

#7
miles_driven = int(input("Enter your driven miles"))
gog = int(input("Enter your amount of gallons used"))
MPG = miles_driven / gog
print(MPG)

print("////////////////////////////////////////////////////////////////")

#10
S = float(1.5) / float(48)
B = float(1) / float(48)
F = float(2.75) / float(48)

cookie = input("How many cookies would you like to make?")

totalS = float(S) * float(cookie)
totalB = float(B) * float(cookie)
totalF = float(F) * float(cookie)

print("You will need the following for your selected amount of cookies")
print("cups of sugar")
print(totalS)
print("cups of butter")
print(totalB)
print("cups of flour")
print(totalF)

