# prompt user to generate a name or quit
# choose a first name at random from list of first names
# assign the name to a variable (first)
# choose a surname at random from list of last names
# assign surname to a variable (last)
# print complete name
# prompt the user to generate another name or quit

import sys, random

print("Welcome to the Silly Name Generator \n")

first_name = ('Bradley', 'Bill', 'Bailey', 'Linda', 'Mary', 'Patricia', 'Jennifer', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Lisa', 'Nancy', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Chris', 'Charles', 'Daniel')

last_name = ('Jones', 'Jackson', 'James', 'Roberts', 'Smith', 'Johnson', 'Williams', 'Brown', 'Garcia','Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris')

answer = input("Would you like to generate a name? ")

while answer.lower() == "yes":
    first = random.choice(first_name)
    last = random.choice(last_name)
    print("Generated Name: " + first + " " + last + "\n \n")
    answer = input("Would you like to generate another name? ")

print("You have quit the random name generator. Goodbye. \n")