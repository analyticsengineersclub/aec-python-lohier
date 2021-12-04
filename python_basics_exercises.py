#While Loop
x = 0
while x < 5:
    print(x)
    x+=1

#Loop over Dictionary
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
for key in cal_lookup:
    print(key + ": " + str(cal_lookup[key]))

#Is Odd or Even
def is_odd(x):
    if (x%2 == 1):
        return True
    else:
        return False

def is_even(x):
    if(x%2 == 0):
        return True
    else:
        return False    

#Conditionals
y = 5
x = 4
def describe_evenness(x):
	if is_even(x):
		print("It’s even!")
	elif is_odd(x):
		print("It’s odd!")
	else:
		print("It’s neither even nor odd!")

#Variable Type
my_first_list = ['apple', 1, 'banana', 2]
def variable_type (variable_list):
    new_list = []
    for variable in variable_list:
        if (type(variable) == int):
            v_squared = variable**2
            new_list.append(v_squared)
        else:
            calories = cal_lookup[variable]
            new_list.append(calories)
    return new_list

#Function
def sq_dict_values(my_dictionary):
    for key in my_dictionary:
        print(my_dictionary[key]**2)