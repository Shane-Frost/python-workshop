apples = input("How many apples? ")
weight = input("KG or LBS? ")
appleWeight = (1/5)
answer = int(apples) * appleWeight

#1kg = 2.2 lbs

if weight == "KG":
    print("You have " + str(answer) + "KG of apples")
elif weight == "LBS":
    print("You have " + str(answer) + "LBS of apples")