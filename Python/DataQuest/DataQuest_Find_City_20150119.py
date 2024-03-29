## DataQuest_Find_City_20150119

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Chapter 2

# Basics: Find the US city with the lowest crime rate --(Find_city_with_lowest_crime_rate)

# Learn about reading in files, parsing the csv format, if statements, and for loops while finding the US city with the least violent crime.  

#####################################

Overview of Useful code:

Title. (searchable)
Data Types. (The_basics)
Open csv files. (Open_csv_files)
String splits. (String_split)
For Loops, lists. (For_Loops)
List of Lists. (List_of_lists)
For Loops, adding to lists. (For_loop_adding_to_lists)
Parse a csv into a _list of lists. (Parse_csv_file)
Count rows _in full data. (Count_rows_in_csv)
Count columns _in full data. (Count_columns_in_csv)
Using _for _and _if statements together. (Using_if_statements_to_find_smallest_value_in_list)
Convert data types, sting to intiger. (Converting_data_types)
Convert your csv numeric values to integers. (Convert_csv_to_integers)
Function _for _min value. (Finding_lowest_crime_rate)
Search a _list of lists _for that _min value. (Searching_a_list_of_lists)
Complete code _for finding the city _with the lowest crime rate. (Find_city_with_lowest_crime_rate)

#####################################

#### SUMMARY OF USEFUL CODE ####

#### The_basics ####

a = type(1)
>>> #integer
b = type("racecar")
>>> #string
c = type(10.6)
>>> #float
d = type([1, "I'm a string in a list!", 5.1])
>>> #list

#### Open_csv_files ####

f = open("test.txt", "r")
a = f.read()

#### String_split ####

a_string = "This\nis\na\nstring\n"
split_string = a_string.split('\n')
print(split_string)
>>> #['This', 'is', 'a', 'string', '']

#### For_Loops ####

a = [5, 10, 15]
for i in a:
    print(i)

#### List_of_lists ####

# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(lolists[0][0])
>>> #1
# Pulls out the third element in the second list.
print(lolists[1][2])
>>> #14

#### For_loop_adding_to_lists ####

# We can setup an old list with items, and an empty new list.
old_list = [1,2,5,10]
new_list = []

# At the end of this loop, new_list will be equal to old_list.
# The loop will have gone through each item in old_list, starting from index 0, and appended it to the end of new_list.
for item in old_list:
    new_list.append(item)
print(new_list)
>>> [1,2,5,10]

#### Parse_csv_file ####

f = open('crime_rates.csv', 'r')  #open file
data = f.read()                   #read file
rows = data.split('\n')           #split data into rows, a list of strings. ['Albuquerque, 749', 'Anaheim, 371', ...]
full_data = []                    #create empty list
for item in rows:
	full_data.append(item.split(","))  #split rows into full_data, a list of lists of strings. [['Albuquerque', '749'], ['Anaheim, 371'], ...]

print(full_data[15][0])           #print the first element(index 0) of the 15th list.
>>> Corpus Christi

#### Count_rows_in_csv ####

count = 0
for item in full_data:
    count = count + 1
print(count)
>>> 73

#### Count_columns_in_csv ####

count = 0
first_row1 = full_data[0]
for columns in first_row1:
    count = count + 1
print(count)

#### Booleans_equality_largerthan_smallerthan ####

a = 10
b = 20
c = 12
d = 8

equality = a == b - a #True
bigger_than = a > b - c  #True
smaller_than = a < b + d  #True

#### Using_if_statements_to_find_smallest_value_in_list ####

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]

#Set the smallest_item variable equal to the lowest value in a.
#Use a for loop to loop through a.

print(max(a))
print(min(a))
smallest_item = max(a)
for item in a:
    if item < smallest_item:
        print(item)
        smallest_item = item

print(smallest_item)

#### Converting_data_types ####

a = ['10', '15', '20', '35']  #List of strings
new_a = []
# Convert all the values in a into integers using a for loop. append them to new_a.
for item in a:
    print(type(item))
    new_a.append(int(item))

for item in new_a:
    print(type(item))

#### Convert_csv_to_integers ####

# We need to convert the crime rate values from our csv file into integers.
# They are strings now because we originally split them up from a large string we read in.

# Here's our csv reading code from before
f = open('crime_rates.csv', 'r')
data = f.read()
print(type(data)) #string
rows = data.split('\n')
print(type(rows)) #list
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1]) #converts string to int
    full_data.append(split_row)
print(type(split_row)) #list
print(type(split_row[1])) #int

#### Finding_lowest_crime_rate ####

# We now know everything we need to find the smallest crime rate.

lowest_crime_rate = 10000
# Set lowest_crime_rate equal to the lowest crime rate in full_data.
# Use for loops and if statements like we did in the last screen.
# You'll also need to the index the second item in each row inside the loop.

for item in full_data:
    if item[1] < lowest_crime_rate:
        lowest_crime_rate = item[1]
    print(lowest_crime_rate)
print("the real lowest crime rate is " + str(lowest_crime_rate))

#### Searching_a_list_of_lists ####

# Can you write code to find the second element in the inner list whose first element is 7? (search through lolist)
lolist = [[1,5,7],[10,8,9],[7,10,11]]
value = 0
for item in lolist:
    if item[0] == 7:
        value = item[1]
    print(value)


#### Find_city_with_lowest_crime_rate ####


# We know that the lowest crime rate is 130.
# This is the second column of the data.
# We need to find the corresponding value in the first column -- the city with the lowest crime rate.

# Let's load the csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

city = ""

# Assign the city with the lowest crime rate to city

lowest_crime_rate = 100000
cities = []

for item in full_data:
    if item[1] < lowest_crime_rate:
        lowest_crime_rate = item[1]
print("the real lowest crime rate is " + str(lowest_crime_rate))

for item in full_data:
    if item[1] == lowest_crime_rate:
        city = item[0]
        cities.append(city)
print(cities)



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#### The_basics ####

# A number without decimals is an integer type.
# An integer can hold negative and positive values
# We can do do math with integers.
a = 5
b = -1
print(a * b)

# Anything enclosed in single or double quotes is a string.
# Strings hold text.
# We can't do math with strings like we can with integers.
# But there are some operations we can do (that we will learn later on).
c = "I am a string.  I do string-like things."
d = 'Also a string!'

# Floats are numbers with decimal points.
e = 5.1
f = 10.2
g = e * f

# There are other types that we will learn about later on.

h = 1
i = "hello"
j = 1.2

########

# The type function has only one input value.
a = type(5)

# The above code invokes the type function on the input 5, and as the output, we get the type of 5.
# The type is assigned to a.


# We can also invoke functions on variables.
b = "DataQuest is the best thing ever"
# Note how when the type for b is printed, it is abbreviated to str.
print(type(b))

c = type(1)
d = type("racecar")
e = type(10.6)

#### ####

# We can assign new values to existing variables.
# It doesn't matter if the new values are different types -- they will still overwrite the variable.

#### ####

# We can print out values and variables.
print(5)
a = 5
print(a)

# Notice how two lines appeared in the results area?
# We can also print some values that will take up multiple lines.
# The \n character means 'make a new line'
print("Hello.\nGoodbye.")
print("Good evening")

#### ####

# Comments aren't executed, so debug mode skips them.
# But other lines can be stepped through.
print(10)
a = 10
print(a)

c = range(0,10)
for item in c:
    print(item)


############################### Python 2 or Python 3

# The major difference that you will immediately notice between python 2 and 3 is the print function.
# The function below will work in Python 2 and 3.
print(10)

# This will only work in Python 2, and is called a print statement.
# It will cause an error in Python 3, as you can see to the right.
print 10

# For now, you don't need to worry too much about Python 2, but it's good to be aware of the differences.

################################################################################

#### Open_csv_files ####

# We can open files with the open function.
# The open function returns a file object, which we store in a variable so that we can use it later.
a = open("test.txt", "r")
print(type(a))

# We can use the .read() method to read the data in the file into a variable.

# Methods are different from functions in that they are associated with a specific object.

# We will get more into objects and classes later on, but for now, it is enough to know that methods act on objects, whereas functions are global, and unattached to any specific objects.

#### ####

# We assign the file object to the variable f.
f = open("test.txt", "r")

# We can then use the .read() method on the file object to read the contents of the file.
# Objects are code constructs that have methods that can act on them.
# We'll make our own objects later on (and in fact, strings, ints, and floats are all objects that have their own special method)
a = f.read()

# We can print out a.
# a is just a string -- it has the entire contents of the file test.txt.
print(a)

################################################################################

#### Lists_the_basics ####

example_list = [index_0, index_1, index_2]

example_list[0]
>>> index_0

# We can make an empty list with square brackets
a = []

# We can also initialize a list with values inside of it
b = [1, "I'm a string in a list!", 5.1]
c = [1,2,3]

# Make a list d that contains all integer values.
# Make another list e containing all string values.
# Make a final list f containing all float values.

d = [1,2,3,4,5]
print(type(d))
print(type(d[0]))
e = ["a","b","c"]
print(type(e))
print(type(e[1]))
f = [1.2,1.3,1.4]
print(type(f))
print(type(f[2]))

# We can get values from lists by using an index.
sample_list = [10, "Boris Yeltsin", 50]
b = sample_list[0]

c = [1, "Mikhail Gorbachev", 10.5]

d = c[0]
e = c[1]
f = c[2]

print(d,e,f)

#### String_split ####

# The .split method takes a character as input, and then turns a string into a list of strings

# We can split a string into a list.
a_string = "This\nis\na\nstring\n"
split_string = a_string.split('\n')
print(split_string)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Read the "crime_rates.csv" file in, split it on the newline character (\n), and store the result into the rows variable.

f = open("crime_rates.csv","r")
a = f.read()

rows = a.split('\n')

#### For_Loops ####

# We can loop over lists using the for i in the_list: notation.

# We can loop over each item in a list.
a = [5, 10, 15]
for i in a:
    print(i)

# The whole block underneath a for loop needs to be indented 4 spaces, and is run once for each item in the list.

the_list = [3,5,8,10,15,17,19]

for item in the_list:
    print(item)

# We can have multiple lines underneath a for loop.
# The code above will go through the_list.
# At the end, sum will equal the sum of all of the items in the list doubled.
the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    # Double the value of i.
    double_i = i * 2
    # Add the doubled value to the sum.
    sum = sum + double_i
print(sum)

## Set the sum variable equal to the sum of all the values tripled.

the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    triple_i = i * 3
    sum = sum + triple_i
print(sum)

#### List_of_lists ####

# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# We can pull out the first element of the list, which is [1,2,3].
# Since [1,2,3] is a list, we can also index it to get elements out.
a = lolists[0]
b = a[0]

value_1_0 = lolists[1][0]
print(value_1_0)
value_1_2 = lolists[1][2]
value_2_0 = lolists[2][0]
value_2_2 = lolists[2][2]



# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# Pulls out the first element in the first list.
a = lolists[0][0]

# Pulls out the third element in the second list.
b = lolists[1][2]

# We can also directly do math with expressions.
c = lolists[0][2] + 10

# Any expression in python can be manipulated without first assigning it to a variable.
d = 10

# Set e equal to d times the first element in the third inner list of lolists.

e = d * lolists[2][0]

#### For_loop_list_of_lists ####

lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

for inner_list in lolists:
    # This will loop through and print each inner list, starting from the one at index 0.
    print(inner_list)

#Use a for loop to print the first element of each inner list.
for inner_list in lolists:
    print(inner_list[0])

#### For_loop_adding_to_lists ####

# The append method adds items to the end of lists.
# list 'a' will go from having no items in it to having 10 at index 0.
a = []
print(a)
a.append(10)
print(a)

# b will go from having one item to having two items.
b = [30]
print(b)
b.append(50)
print(b)

# We can setup an old list with items, and an empty new list.
old_list = [1,2,5,10]
new_list = []

# At the end of this loop, new_list will be equal to old_list.
# The loop will have gone through each item in old_list, starting from index 0, and appended it to the end of new_list.
for item in old_list:
    new_list.append(item)
print(new_list)

c = [20,30]

#append 60 to c. Then append 70 to c. c should end up with 4 items.

c.append(60)
c.append(70)
print(c)

################################################################################

#### Parse_csv_file ####

#Splitting the csv file into columns
#When we left off with parsing our csv file, we had split it into rows, but still had to split up the strings we were left with into columns.
#We can use the .split method, along with our newfound knowledge of for loops and lists of lists, to split up the file.

# We can use the .split method, with a comma as an input, to split a string on a comma.
# a_list is a list with 1,10,15, and 20 as elements.
a_string = "1,10,15,20"
a_list = a_string.split(",")
print(a_list)
>>> ['1','10','15','20']
print(type(a_list))
>>> <class 'list'>
print(a_list[0])
>>> 1

# We split our csv file data into rows earlier.
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []

#Instructions
#split each string in the list rows and append the result to full_data.
#At the end, full_data will be a list of lists containing the rows and columns in the csv file.
#You'll need to use for loops.

for item in rows:
	full_data.append(item.split(","))

# I now have a list of lists

print(full_data[15][0])
>>> Corpus Christi


#### Count_rows_in_csv ####

# Remember how we counted the length of our list before?
# When the loop finishes, count will be equal to 5, which is the number of items in the_list.
# This is because 1 will be added to count for every iteration of the loop.
the_list = [5,6,10,13,17]
count = 0
for item in the_list:
    count = count + 1
print(count)

print("Now count rows in crime rates csv file")
count = 0
# We can parse our csv file like we did before.
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    count = count + 1
print(count)
>>> 73

print("now full data")
count = 0
for item in full_data:
    count = count + 1
print(count)
>>> 73


## Visualizing the data as a table

# Mental mapping between a list of lists and a table.
# list[0][0] is the first element of the first list.
# table(0,0) is the top left cell of the table.
# The indexing is the same, so the mapping is relatively easy.


#### Count_columns_in_csv ####

# We just counted the number of rows.  We can do the same for the number of columns.
# Let's create a list of lists, and assume that the inner lists are the rows.
# If this is the case, the number of columns is the number of items in any row.
l = [[1,2,3],[3,4,5],[5,6,7]]
first_row = l[0]
count = 0
for column in first_row:
    count = count + 1
print(count)

# Count is now equal to 3, the number of items in the first row of data.
# All of the rows have the same number of items, so 3 is our column count.

# We parse our csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0
first_row1 = full_data[0]
for columns in first_row1:
    count = count + 1
print(count)

################################################################################

## Booleans, True or False

# You can use = to assign a value to a variable. eg. a = 5, assign a to the numeric value 5.
# you can use == to compare equality. eg. 4 == 5 >>> False. 5 == 5 >>> True
b = 7
b == 6
>>> False
b == 7
>>> True

# Allows us to run certain segments of code if something is True and not run it if it is False. Helps makes our programs powerful.

# Booleans are statements that take on either True or False as a value.
# We can create booleans by comparing two values and seeing if they are equal
# This will be False
print("Andre the Giant" == "Short")

# This is True
print("Andre the Giant" == "Andre the Giant")

# True and False are special python keywords of the boolean type.
# Boolean is abbreviated to bool.
print(type(True))
print(type(False))

a = 10
b = 5

# False
print(a == b)

# True
print(a == 10)

# Assigning a boolean to a variable
c = a == b
print(c)

d = a == 10  #True
e = b == 5  #True
f = b == a  #False
g = a == a - b  #False

## Using greater than signs

# This will be True
print(5 > 4)

# This is False
print(4 > 5)

# We can also assign these values to variables
# The value of a will be True, and it will be a boolean type
a = 5 > 4
print(a)
print(type(a))

b = 5 > 1  #True
c = 100 > 1000  #False

# Just like with the greater than sign, we can use the less than sign.
print(4 < 5)
print(5 < 4)

# We can assign these values to variables.
# They will be of the boolean type.
a = 4 < 5
print(a)
print(type(a))

b = 15 < 122  #True
c = 15 < 12  #False

#### Booleans_equality_largerthan_smallerthan ####

a = 10
b = 20
c = 12
d = 8

equality = a == b - a #True
bigger_than = a > b - c  #True
smaller_than = a < b + d  #True

################################################################################

# The if statement.
#when the if statement is True > do stuff, when if is False > do not do stuff.

a = [70,80,90,100]

for i in a:
    if i > 99:
        print("Alert")

# Lets us conditionally run code.
a = 10
b = 10
if a == b:
    print("equal")

if a == 12:
    print("12")

>>> equal

#### Boolean_in_if_statements ####

# If statements are followed by a boolean, which evaluates to True or False.
# If the boolean is True, the code is run.
# Otherwise, it isn't.
# Success! will be printed here.
if 4 == 4:
    print("Success!")

# Nothing will be printed here, because 10 doesn't equal 8.
if 10 == 8:
    print("No success!")

#Write an if statement whose boolean statement evaluates to True and prints out "Hello world!"

if "happy" == "happy":
    print("Hello world!")

# We can also use if statements with boolean statements containing variables.
# The if statement below will print "Success!" because a == 4 evaluates to True.
a = 4
if a == 4:
    print("Success!")

# This will print nothing, because b > 10 is False.
b = 10
if b > 10:
    print("No success!")

c = 15
if c > 1:
    print("Much success!")


#### Using_if_statements_to_find_smallest_value_in_list ####

# We can 'nest' if statements inside for loops, or vice versa.
the_list = [5, 10, 15, 20]

# Let's say we want to count how many elements in the_list are greater than 10.
count = 0
for item in the_list:
    if item > 10:
        count = count + 1
print(count)

# Count equals two because item > 10 evaluated to True for 2 of the items in the_list.
# Notice how we indented the body of the if statement another 4 spaces.
# Whenever you put statements that have indented blocks inside each other, you will need to indent 4 more spaces.

a = 2

# Let's say we want to print all of the elements in the_list if a > 1.
if a > 1:
    for item in the_list:
        print(item)

# The above code will print all of the items in the_list, because a > 1 evaluates to True.

# Write a for loop that prints out all of the items in the_list that are greater than 5.

for item in the_list:
    if item > 5:
        print(item)

# We can use for loops and if statements to find the smallest value in a list.
the_list = [20,50,5,100]

# Set smallest_item to a value that is bigger than anything in the_list.
smallest_item = 1000
for item in the_list:
    # Check if each item is less than smallest_item.
    if item < smallest_item:
        # If it is, set smallest_item equal to its value.
        smallest_item = item
print(smallest_item)

# The first time through the loop above, smallest_item will be set to 20, because 20 < 1000 is True.
# The second time through, smallest_item will stay at 20, because 50 < 20 is False.
# The third time through, smallest_item will be set to 5, because 5 < 20 is True.
# The last time through, smallest_item will stay at 5, because 100 < 5 is False.

smallest_item = 1000
a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]

#Set the smallest_item variable equal to the lowest value in a.
#Use a for loop to loop through a.

print(max(a))
print(min(a))
smallest_item = max(a)
for item in a:
    if item < smallest_item:
        print(item)
        smallest_item = item

print(smallest_item)


#### Converting_data_types ####

# We can convert between different data types
# The int() function will convert an object to an integer

# There's one problem with our parsed CSV file -- because we parsed it from a string, all of the values are stored as strings.
# (go to the csv parsing and check types if you want to verify)
# We need the crime rate column as an integer so we can work with it.

# We can use the int() function to turn a string into an int.
# It only works with strings that have int values inside them.
a = '5'
print(type(a))

# a is a string containing the integer '5'.
# We can use the int function to parse it into the integer 5.
b = int(a)
print(b)
print(type(b))

c = '10'
d = '20'
e = '30'

c_int = int(c)
d_int = int(d)
e_int = int(e)

# Now that we know about the int() function, let's use it to convert the values in a list to integers.
the_list = ['1', '2', '3']
new_list = []

# Loop through the_list
for item in the_list:
    # Get the int value of the item in the list
    item_int = int(item)
    # Add the int item to the new list
    new_list.append(item_int)
# Print out the new list
print(new_list)

a = ['10', '15', '20', '35']
new_a = []

# Convert all the values in a into integers using a for loop. append them to new_a.

for item in a:
    print(type(item))
    new_a.append(int(item))

for item in new_a:
    print(type(item))

#### Convert_csv_to_integers ####

# We need to convert the crime rate values from our csv file into integers.
# They are strings now because we originally split them up from a large string we read in.

# Here's our csv reading code from before
f = open('crime_rates.csv', 'r')
data = f.read()
print(type(data)) #string
rows = data.split('\n')
print(type(rows)) #list
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1]) #converts string to int
    full_data.append(split_row)
print(type(split_row)) #list
print(type(split_row[1])) #int

#### Finding_lowest_crime_rate ####

# We now know everything we need to find the smallest crime rate.
# Remember that we are finding the smallest crime rate (second column), not the city (first column) with the lowest crime rate.
# We parse our csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

# We now know everything we need to find the smallest crime rate.
lowest_crime_rate = 10000

# Set lowest_crime_rate equal to the lowest crime rate in full_data.
# Use for loops and if statements like we did in the last screen.
# You'll also need to the index the second item in each row inside the loop.

for item in full_data:
    if item[1] < lowest_crime_rate:
        lowest_crime_rate = item[1]
    print(lowest_crime_rate)
print("the real lowest crime rate is " + str(lowest_crime_rate))

#### Searching_a_list ####

# We can search a list for a given value
the_list = [5, 6, 7, 10, 50]

# Loop through the_list
for item in the_list:
    # If the list item equals 5, print out "Found"
    if item == 5:
        print("Found")

# The above code will print "Found" once.

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]

for item in a:
    if item == 78:
        print("Yes")

#### Searching_a_list_of_lists ####

lolist = [[1,5,7],[10,8,9],[7,10,11]]

# Let's say we want to get the first element of the inner list whose third element is 9.
value = 0
for item in lolist:
    last_value = item[2]
    first_value = item[0]
    if last_value == 9:
        value = first_value
print(value)

# The above code will print 10, which is the first value in the inner list where 9 is the last value.
# What we are doing can also be described in terms of rows and columns.
# We are finding the first column in the rows where the third column equals 9.

# Can you write code to find the second element in the inner list whose first element is 7? (search through lolist)
# Set the value variable equal to the answer.
value = 0

# Find the second element in the inner list whose first element is 7.
# You'll need to search through lolist to do it.
# Assign the answer to the value variable.

for item in lolist:
    if item[0] == 7:
        value = item[1]
    print(value)



#### Find_city_with_lowest_crime_rate ####

# We know that the lowest crime rate is 130.
# This is the second column of the data.
# We need to find the corresponding value in the first column -- the city with the lowest crime rate.

# Let's load the csv file
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

city = ""

# Assign the city with the lowest crime rate to city

lowest_crime_rate = 100000
cities = []

for item in full_data:
    if item[1] < lowest_crime_rate:
        lowest_crime_rate = item[1]
print("the real lowest crime rate is " + str(lowest_crime_rate))

for item in full_data:
    if item[1] == lowest_crime_rate:
        city = item[0]
        cities.append(city)
print(cities)






