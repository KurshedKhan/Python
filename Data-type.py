# variable in python

num = 10

# print() is a method, for display message and variable.
print("This is a number variable : ",num)


# type() is a method, for check our data type in our variable.
type(num)
# num is a integer type data-type

# id() is a method, This ID is akin to the memory address of the object.
id(num)

"""
function id() returns the identity of an object.
"""

# Data type in Python

# Number ==> 1.Integer Data type
#               a.Boolean Data type
#            2.Floating Data type
#            3.Complex Data type

#Interger Data type :
number = 10
print("This is Interger : ",number)

#Floating Data type :
floating = 10.5
print("This is floating number : ",floating)


#Complex Data type :
complex1 = 3 + 2j
print("This is complex number : ",complex1)


#Boolean Data type :
isOdd = True # Keyword ==> True
print("Boolean true :",isOdd)
isEven = False # Keyword ==> False
print("Boolean false : ",isEven)


# Sequence Data type :
#                       1.String Data type
#                       2.List Data type
#                       3.Tuple Data type

# String Data type :
message = "smile face"
print("String :",message)
roll = "123"
print("String roll number formate :",roll)
type(roll) # string data type, not integer data type

#List Data type :
list1 = [10,20,"New Dehli","20C",]
print("list  : ",list1)
print(list1[2]) # list,item accessing by indexing in also integer form.

#Tuple Data type : () ==> parenthesis
tuple1 = (10,20,30,"New Dehli","20C")
print("tuple :",tuple1)


# Set Data type :
set1 = {10,20,10.5,"20C","New Dehli"}
print(set1)

# duplicate value :
set2 = {1,2,1,3,2,1,5}
print(set2)


# None data type : absence of value in a situation.
school = None
print(school)

# Mapping Data type : key:value pairs
#   1.Dictionary Data type

Dict1 = {
            "Name" : "Avi",
            "Age"   : 17,
            "Height" : 5.4

        }

print(Dict1)
print("Name : ",Dict1["Name"])









