
# check to see if string contains another string
str1 = "i ate some food"
str2 = "food"
str3 = "piza"

def string_check(str1, str2):
    if str2 in str1:
        print(f'"{str1}" contains "{str2}"')
    else:
        print(f'"{str1}" dose not contain "{str2}"')

string_check(str1, str2)
string_check(str1, str3)
string_check(str3, str1)

# recursive function that takes a number and returns the sum of numbers from 0 to the number

def sum_finder(n):
    if n == 1:
        return(1)
    else:
        sum = n + sum_finder((n - 1))
        return(sum)

print(sum_finder(6))

# return a string reversed

def reverse_string(str):
    return str[::-1]

print(reverse_string(str1))

# Write a recursive function that takes in a list of strings and returns the words capitalized

def capitalizer(words):
    for word in words:
        capitalize = word.upper()
        print(capitalize)

words = ['wpresd', 'foods', 'stuff']

capitalizer(words)