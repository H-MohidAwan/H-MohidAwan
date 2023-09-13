""" Module Description: This module is for python learning practices. """
# variable assignment
X = 10
Y = 3

# **************************************************************datatypes************************

# ------------------------------------------------------------------ Numeric type Datatypes------
age_int = 29   # pylint: disable=invalid-name
height_float = 5.8  # pylint: disable=invalid-name
num_complex = 3 + 3j  # pylint: disable=invalid-name
# print(age_int, type(age_int))
# print(height_float, type(height_float),)
print(num_complex, type(num_complex))

# --------------------------------------------------------------- String type Datatypes----------
name_str = 'bilal'  # pylint: disable=invalid-name
# print(name_str, type(name_str))

# -------------------------------------------------------------- Sequence type Datatypes----------
students_list = ['bilal', 'umair', 'fahad', 'ali', 'khalid', 'fahad']
num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
attendance_tuple = ('P', 'A', 1, 0)
data_range = range(1, 10)
# print(students_list, type(students_list),)
# print(num_list, type(num_list),)
# print(attendance_tuple, type(attendance_tuple),)
# print(data_range, type(data_range),)

# --------------------------------------------------------------- Mapping type Datatypes----------
person_dict = {'name': 'ali', 'age': 10, 'city': 'lahore', 'student': True}
# print(person_dict, type(person_dict),)

# ----------------------------------------------------------------- Boolean type Datatypes--------
is_student_bool = True   # pylint: disable=invalid-name
# print(is_student_bool, type(is_student_bool),)

# ---------------------------------------------------------------- Set type Datatypes-------------
int_set = {1, 2, 7, 4, 8, 6, 3, 5, }
int_set = frozenset({1, 2, 7, 4, 8, 6, 3, 5, })
str_set = set('hello str set')
# print(int_set, type(int_set),)
# print(str_set, type(str_set),)

# -------------------------------------------------------------- Binary type Datatypes-----------
binary_data_bytes = b'hello'      # pylint: disable=invalid-name
binary_data_bytearray = bytearray(b'hello')  # pylint: disable=invalid-name
binary_data_bytearray = memoryview(b'hello')  # pylint: disable=invalid-name
# print(binary_data_bytes, type(binary_data_bytes),)
# print(binary_data_bytearray, type(binary_data_bytearray),)

# ----------------------------------------------------------------- None/Null type Datatypes------
datatype_none = None     # pylint: disable=invalid-name
# print(datatype_none, type(datatype_none),)

# placeholder_ellipsis = ellipsis

# **************************************************************Operators************************

# -----------------------------------------------------arithmetic operators--------------------
sum_result = X + Y  # pylint: disable=invalid-name
difference = X - Y  # pylint: disable=invalid-name
product = X * Y  # pylint: disable=invalid-name
division = X / Y  # pylint: disable=invalid-name
remainder = X % Y  # pylint: disable=invalid-name
exponentiation = X ** Y  # pylint: disable=invalid-name
# print(sum_result, difference, product, division, remainder, exponentiation)
# print(type(sum_result), type(difference), type(product),
#       type(division), type(remainder), type(exponentiation))


# ------------------------------------------------------comparison operators--------------------
is_equal = X == Y  # pylint: disable=invalid-name
not_equal = X != Y  # pylint: disable=invalid-name
less_than = X < Y  # pylint: disable=invalid-name
greater_than = X > Y  # pylint: disable=invalid-name
less_than_equal = X <= Y  # pylint: disable=invalid-name
greater_than_equal = X >= Y  # pylint: disable=invalid-name
# print(is_equal, not_equal, less_than, greater_than,
#       less_than_equal, greater_than_equal)


# -------------------------------------------------------logical operators----------------------
is_student = True   # pylint: disable=invalid-name
has_passing_grade = True    # pylint: disable=invalid-name
is_enrolled = True  # pylint: disable=invalid-name

eligible = is_student and has_passing_grade  # pylint: disable=invalid-name
allowed = is_enrolled or has_passing_grade    # pylint: disable=invalid-name
not_eligible = not eligible                   # pylint: disable=invalid-name
# print(eligible, 'eligible')
# print(allowed, 'allowed')
# print(not_eligible, 'not_eligible')


# ************************************Practice questions from chatGPT***************************

# name = input('Enter your Name ')          # pylint: disable=invalid-name
# age = int(input('Enter a Year You were born in  '))
# current_year = 2023  # pylint:disable=invalid-name
# age_cal = current_year - age
# height = input('Enter your Height ')      # pylint: disable=invalid-name
# print(f"My name is {name},I'm {age_cal} years old and {height} feet tall.")
# # print("my name is {}, I'm {} years old and {} feet tall".format(name, age, height))

# quote = input('Enter a Famous Quote  ')  # pylint: disable=invalid-name
# print(f'A famous quote """{quote}""" By {name}')

# temperature = 30.5  # pylint: disable=invalid-name
# print(f"it's {temperature} degree celsius out there")

# fruits = ['apple', 'bannana', 'orange']
# print(f"second fruit of a list is {fruits[1]}")

# coordinates = (31.520370, 74.358749)
# print(f"""coordinates of current location are latitude =
#        {coordinates[0]} and longitude = {coordinates[1]}""")

# radius = 2      # pylint: disable=invalid-name
# PI = 3.14159       # pylint: disable=invalid-name
# circle_area = PI*(radius**radius)      # pylint: disable=invalid-name
# print(f"if radius = {radius}, area of a circle = {circle_area}")

# test1, test2, test3 = 100, 300, 600  # assign value to variables in single line
# avearge_test_num = (test1+test2+test3)/3        # pylint: disable=invalid-name
# print(f"avearge numbers of three tests is {avearge_test_num}")

# celsius = 35.5      # pylint: disable=invalid-name
# fahrenheit = (celsius*9/5)+32  # pylint: disable=invalid-name
# print(f'{celsius} degree celsius is equal to {fahrenheit} degree fahrenheit')
