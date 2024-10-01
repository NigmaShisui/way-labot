wow = int(input("Number of your favorite fruites? "))
fruits = []


for x in range(wow):
    fr = input("Your Fav fruites?")
    fruits.append(fr)

for i in fruits:
    print(i)
    if i == "banana":   
        break
    elif i == "apple":
       print("Happy Eating")