
def return_10():
	return 10
	
def add(x, y):
	return x+y
	
def subtract(x, y):
	return x-y
	
def multiply(x, y):
	return x*y

def divide(x, y):
	return x/y
	
def length_of_string(mystring):
	return len(mystring)

def join_string(word1, word2):
	return word1 + word2

def add_string_as_number(num1, num2):
	return int(num1) + int(num2)

def number_to_full_month_name(num):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	return months[num-1]
	
def number_to_short_month_name(num):
	return number_to_full_month_name(num)[0:3]

def volume_of_cube(a, b, c):
	return a*b*c

def reverse_string(mystring):
	return mystring[::-1]

def fahrenheit_to_celsius(temp):
	return (5/9 * (temp-32))