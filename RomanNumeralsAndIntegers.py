# Task 1: Roman numerals To Integers.
# Creating user define Functions to Convert Roman Numerals To Integers.
def romanToInt(s):    
      #Creating a Dictionary for Every possible Values of Roman Numerals (In Uppercase Alphabet as well as in Lowercase Alphabet)
      roman = {'I':1,'i':1,'V':5,'v':5,'X':10,'x':10,'L':50,'l':50,'C':100,'c':100,'D':500,'d':500,'M':1000,'m':1000,'IV':4,'iv':4,'IX':9,'ix':9,'XL':40,'xl':40,'XC':90,'xc':90,'cd':400,'CD':400,'cm':900,'CM':900} 
      # Intialising variable i with 0 and variable num with 0 for the end result.
      i = 0
      num = 0
      # Using while loop 
      while i < len(s):
        # Using Conditional Statements (if/else) to satisfy the given condition.
        if i+1<len(s) and s[i:i+2] in roman: 
            num= num + roman[s[i:i+2]]
            i= i + 2
        else:
            num= num + roman[s[i]]
            i= i + 1
      # Returning the value in Variable num, and the Return type is Int.
      return num
# Using input() function to ask the user for Roman Numeral to convert it into integer.
x=input("Enter a Roman Numeral: ")
# Using print() function to print the converted value.
print("The Corresponding Value of The Roman Numeral",x," in Integer is", romanToInt(x))


# TASK 2 : INTEGERS TO ROMAN NUMERALS
# Creating user define function to Convert the Integers to Roman Numerals. 
def IntToRoman(a):
    # Initialising j with 0 and p with empty string.  
   j=0
   p=""
   # Creating a number list for Distinct Integer Values. 
   number=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
   # Creating a value list for possible Roman Numerals.
   value=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
   # Using while loop. Here in the condition we assigned the integer input to be greater than 0. Since there are no roman numerals less than One. 
   while a > 0:
      div=a//number[j]
      a=a%number[j]
      while div:
         p=p+value[j]
         div=div-1
      j=j+1
    # Returning the Value in Valueble p, and the return type is str.
   return p
# Using input() function to ask the user for the integer to convert it into Roman Numeral.
n=int(input("Enter an Integer :"))
# Using print() function to print the converted value.
print("The Corresponding Value of the Integer",n," in Roman Numeral is ",IntToRoman(n))