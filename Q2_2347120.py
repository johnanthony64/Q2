# list 
price = [i for i in range(1,101)]

divby3 = [i for i in price if i%3==0]
print(len(divby3), "numbers divisible by 3:")

sq= [ i**2 for i in price if i%2==0 ] 
print("\n sqaure of", len(sq), "even numbers:\n",sq)

s = sum ([i for i in price if i%2==0])
print("\n sum of all even numbers:\n", sq)

print ("\n Original list:\n", price)
price= list(set(price))
print("\n Duplicate removed:\n", price, "\n\n")


## Dictionary
def func(food):
    foodexpiry={
        "IceCream": "12 March 2023", 
         "Sweets": "13 April 2023", 
         "Biryani": "24 Sep 2023",
    }
    print("The expiry of", food, "is", foodexpiry[food])

food=input("Enter food name: ")
func(food)
