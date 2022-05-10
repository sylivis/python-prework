#Baily Leary
#Created 5-9-22

#Python Prework Questions

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print(f'Hello_{str(user_name)}!')    


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    n = 1
    while n < 100:
        if n % 25 == 0 or n % 49 == 0:
            print(f'{str(n)}\n')
        else:
            print(f'{str(n)}', end=" ")
        n +=2
    print("\n")


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return sorted(a_list)[-1]


#Question 4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false)

def is_leap_year(a_year):
    a_year = int(a_year)
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0:
            return True
        else:
            return False
    else:
        return False   


#Questaion Five:
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    n = 0
    for a in a_list[:-1]:                            
        n +=1                                                 
        if a + 1 == a_list[n]:         
            answer = True               
        if a + 1 != a_list[n]:          
            answer = False              
            break                                                              
    return answer               



