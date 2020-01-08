description = """
==============================================
This is basic tutorial for python study.
It will include basic syntax and coding style.
Also include the print result
==============================================
"""
section_line = "=====================Section Line====================="
line = "======================================================"
print description
hello_world = "Hello world"
print("Hello world")
# result: Hello world

# Condition tutorial
if 1 > 0:
    print ("Ture, 1 > 0")
else:
    print ("False, 1 < 0")
# result: Ture, 1 > 0

# Same level of spacing will present as same scope
if 0 > 1:
    print ("Ture, 0 > 1")
    print ("Still true case")
else:
    print ("False, 0 < 1")
    print ("Still false case")
# result: False, 0 < 1
#         Still false case

if 0 == 0:
    print ("equal")  # result: equal

# Variable & string formatting
x = 100
y = "Hello World!"
z = 'Hello World!'
if x > 0:
    print ("Ture, {} > 0, {}".format(x,y))
else:
    print ("False, {} < 0, {}".format(x,y))
# result: Ture, 100 > 0, Hello World!

print ("Same perform y: {}, x:{}".format(y,z))  # result: Same perform y: Hello World!, x:Hello World!

print y  # result: Hello World!


# Function print value
def myfunc(value):
    print("myfunc value:{}".format(value))


# Test myfunc
myfunc(y)

print section_line

gvalue = "I am here"


# Global value
def my_global_value():
    global gvalue
    gvalue = "I am not here"


# Test modify global value
print gvalue  # result: I am here
my_global_value()
print gvalue  # result: I am not here

print section_line

# Data types
value_str_a = "String"
value_str_b = 'String'
value_int = 1
value_float = 1.0
value_list_int = [1, 2, 3]
value_list_str = ["one", "two", "three"]
value_list_mix = [1, "two", 3.0]
value_tuple = ("one", "two", "three")  # in order and unchangeable/immutable
value_range = range(0, 12)  # Range from 0 to 12
value_dict = {"value": 0, "name": "mapping"}  # Mapping dictionary
print("value dict value: {}".format(value_dict["value"]))
value_set = {"value", "name"}
value_frozenset = frozenset(value_set)
value_boolean = True
value_byte = b"Hello world!"
value_byte_array = bytearray(5)
value_memory_view = memoryview(value_byte_array)

# Data types with constructor
value_str_a = str("String")
value_str_b = str('String')
value_int = int(1)
value_float = float(1.0)
value_list_int = list([1, 2, 3])
value_list_str = list(["one", "two", "three"])
value_list_mix = list([1, "two", 3.0])
value_tuple = tuple(("one", "two", "three"))
value_range = range(0, 12)  # Range from 0 to 12
value_dict = dict(value=0, name="mapping")  # Mapping dictionary
print("value dict mapping: {}".format(value_dict.get("name")))
value_set = set(("value", "name"))
value_frozenset = frozenset(value_set)
value_boolean = bool(0)  # Logic for boolean, True == not equal to 0
value_byte = bytes(5)
value_byte_array = bytearray(5)
value_memory_view = memoryview(value_byte_array)

print section_line

import random
print("Random number: ".format(random.randrange(1, 100, 2)))  # print random number in 1-100 step 2, which means the result will be odd value

print section_line

print(hello_world[0])  # first char of string
print(hello_world[0:5])  # print string with position
print(hello_world[6:])  # print string with position
print("String length: {}".format(len(hello_world)))

print section_line

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionary looping
for key in thisdict:
    print("Dict key: {}, value: {}".format(key,thisdict[key]))

print line

# Dictionary item looping
for key, value in thisdict.items():
    print("Dict key: {}, value: {}".format(key, value))

print line


def print_dict(dict):
    for key in dict:
        print("Dict key: {}, value: {}".format(key,dict[key]))

thisdict["type"] = "car"
print_dict(thisdict)

print line
print("Delete item")
del thisdict["type"]
print_dict(thisdict)

print line
thisdict["type"] = "car"
print("Delete item")
thisdict.pop("type")
print_dict(thisdict)

lambda_function_add = lambda v1, v2: v1 + v2
print(lambda_function_add(1,2))

print section_line
print "Class init and function test"
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def printObj(self):
        print("{} [brand: {}, model: {}, year: {}]".format(self.__class__.__name__, self.brand, self.model, self.year))


Car("Ford", "Mustang", 1964).printObj()

print line
print "Class Inheritance and pass the definitions"

class Ford(Car):
    pass


Ford("Ford", "Mustang", 1964).printObj()

print section_line
print "Json handling"

import json

json_str = '{ "name":"John", "age":30, "city":"New York"}'
json_dict = json.loads(json_str)
print(json_dict["age"])

print(json.dumps(json_dict))

print section_line

