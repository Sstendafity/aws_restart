# Array
import array as arr

arrs = arr.array('i', [1, 2, 3, 4, 5])
print(arrs)
myArr = arr.array('u', ['a', 'b', 'c'])
print(myArr)
print(type(arrs))
print(type(myArr))
print("\n")


# Exercise 1: Introducing the list data type
myFruitList = ["apple", "banana", "cherry", "durian", "rose apple"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[3] = "orange"
print(myFruitList)
print("\n")


# Exercise 2: Introducing the tuple data type
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
# myFinalAnswerTuple[1] = "orange" (will be error because tuple can't be changed)
print("\n")


# Exercise 3: Introducing the dictionary data type
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

myFavoriteFruitDictionary["Red"] = "watermelon"
print(myFavoriteFruitDictionary)
print(myFavoriteFruitDictionary["Red"])
print("\n")


# List 
myList = [
    [1,2,4], 
    [3,2,1], 
    [4,5,7]
]
print(myList)
print(myList[1][1])
print(myList[0][2])

# Set
print("\nSet")
mySet = {1, 2, 3, 4, 5}
print(mySet)
print(type(mySet))