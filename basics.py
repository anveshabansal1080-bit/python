#===============================================
# PROGRAM 1: VARIABLES
# ==============================================

#name = "anvesha"
#age = 20
#print(name)

#===============================================
# PROGRAM 2: Simple print 
# ==============================================

#print ("Hello World")
#===============================================
# PROGRAM 3: datatype
# ==============================================
name = "anvesha"
age = 20
print(type(name))
print(type(age))
#===============================================
# PROGRAM 4: Addition
# ==============================================
a=2
b=3
sum=a+b
print(sum)
#===============================================
# PROGRAM 5: comment
# ==============================================
print("hello world")
# multi-line 
# comment(ctrl+/) for comment out multiply lines
#===============================================
# PROGRAM 6: operation
# ==============================================
a= int("2")
b = 4.53
sum = a + b
print(sum)
#===============================================
# PROGRAM 7: typecasting
# ==============================================
name=input("enter your name:")
print("welcome",name)  #the output will always be in str can use typecasting to change the datatype
#===============================================
# PROGRAM 8: addition by taking input
# ==============================================
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("sum=", a+b)
#===============================================
# PROGRAM 9: area by taking input
# ==============================================
side=int(input("enter the side:"))
print("area=",side**2)
#===============================================
# PROGRAM 10: concatination (adding of two strings)
# ==============================================
str1="Anvesha"
str2=" Bansal"
print(str1+str2)
#===============================================
# PROGRAM 10: length (count the spaces,signs every single thing)
# ==============================================
str1="Anvesha"
str2=" Bansal"
print(len(str1+str2))
#===============================================
# PROGRAM 11: indexing(acces the element)
# ==============================================
str="Anvesha"
print(str[5])
#===============================================
# PROGRAM 12: slicing & negative slicing(picking the element)
# ==============================================
str="Anvesha Bansal"
print(str[8:15])
print(str[:7])
print(str[8:])
print(str[-14:-7])
#===============================================
# PROGRAM 13:endswith, capitalise,replace, find & count
# ==============================================
str="I am using python language for my coding."
print(str.endswith("ing"))   # tell the ending
print(str.endswith("ing."))

str="i am using python language for my coding."     # capitalises the first letter by making new str
print(str.capitalize()) 
print(str)
str1=str.capitalize()     # # capitalises the first letter in orignal string
print(str1) 

str="I am using python language for my coding."     # replaces the word or element
print(str.replace("python","java")) 

str="I am using python language for my coding."   #finds the index of the word
print(str.find("python"))

str="I am using python language for my coding."    # count the number of repeataton time
print(str.count("my")) 
#===============================================
# PROGRAM 14: taking input finding the len
# ==============================================
name=input("Enter your name")
print("length of my name is:",len(name))
#===============================================
# PROGRAM 15: taking str and count $
# ==============================================
str=("$ i $am $ using python lan$ua$e")
print("total count of $is:",str.count("$"))
#===============================================
# PROGRAM 16: conditional statement
# ==============================================
marks=int(input("Enter total marks of student:"))     #taking inut and grade the student marks
if(marks >= 90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grades of student:", grade)
#===============================================
# PROGRAM 17: nested statement
# ==============================================
age=25
if (age>=18):
    if(age>=80):
        print("can't drive")
    else:
         print("can drive")
else:
    print("can't drive")
#===============================================
# PROGRAM 18: taking input and print even or odd
# ==============================================
num=int(input("enter your number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number")
#===============================================
# PROGRAM 19: taking input and find the greatest number
# ==============================================
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=int(inp"enter your third number:"))

if(a>=b and a>=c):
    print("first number is greatest",a)
elif(b>=c):
     print("second number is greatest",b)
else:
    print("third number is greatest",c)
#===============================================
# PROGRAM 20: taking input and find multiply of 7
# ==============================================
num=int(input("enter your number:"))
if(num%7==0):
    print("mutliply of 7")
else:
    print("not a multiple of 7")
#===============================================
# PROGRAM 21: list 
# ==============================================
marks=[22.5,88.5,55.5,66.5,45.5,26.9]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))
#===============================================
# PROGRAM 22: list are mutable
# ==============================================
student=["arjun",85,"delhi",55.8]
print(student)
student[0]= "anvesha"
print(student)
#===============================================
# PROGRAM 23: list methods
# ==============================================
marks=[22.5,88.5,55.5,66.5,45.5,26.9]
marks.append(52)       #adds the element at last
print(marks)
marks.sort()      #sorts ascending order
print(marks)
marks.reverse()     #reverse the order
print(marks)
marks.insert(1,44)   #inserts the element(index,element)
print(marks)
marks=[55.5,88.5,55.5,66.5,45.5,26.9]
marks.remove(55.5)    #remove the elment occuring firsttime
print(marks)
marks.pop(2)        #popsthe index element
print(marks)
#===============================================
# PROGRAM 24: tuple
# ==============================================
tup=(55.5,88.5,55.5,66.5,45.5,26.9)      # they are immutable, (1,) with, only this will be considered as tuple othrwise it will be int
print(type(tup))
print(tup[1])  
#===============================================
# PROGRAM 25: tuple methods
# ==============================================
tup=(55.5,88.5,55.5,66.5,45.5,26.9)
tup.index(55.5)       #first occurance index
tup.count(55.5)       #count the total times of occurance
#===============================================
# PROGRAM 26: taking input of fav movies and combine them in tuple
# ==============================================
movie=[]
movie.append(input("Enter your favrouite first movie:"))
movie.append(input("Enter your favrouite second movie:"))
movie.append(input("Enter your favrouite third movie:"))
print(movie)
#===============================================
# PROGRAM 27: creating list and checking it is palindrome or not
# ==============================================
list1=["m","a","m"]                    
copy_list1=list1.copy()
list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
#===============================================
# PROGRAM 28: creating a tuple and finding grade a 
# ==============================================
tup=("c","d","a","a","b","b","a")
tup.count("a")
#===============================================
# PROGRAM 29: making the tuple list and sorting them 
# ==============================================
tup=["c","d","a","a","b","b","a"]
tup.sort()
print(tup)
