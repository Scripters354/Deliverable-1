Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> import random
>>> from itertools import islice
>>> import string
>>> prime =[]
>>> my_stNr = 15128271
>>> num_str = list(map(int, str(my_stNr)))
>>> count = 0
>>> 
>>> for num in num_str:
	if num >1:
		for i in range(2, num //2):
			if num % i==0:
				break
			else:
				prime.append(num)
				count +=1
		x = random.randint(25,50)
		r=x/count

		
Traceback (most recent call last):
  File "<pyshell#21>", line 10, in <module>
    r=x/count
ZeroDivisionError: division by zero
>>> for num in num_str:
	if num >1:
		for i in range(2, num //2):
			if num % i==0:
				break
			else:
				prime.append(num)
				count +=1
		x = random.randint(25,50)
		r=x/count
		def randomString(stringLength):
			letters = string.ascii_lowercase
			vowels=0
			for i in letters:
				if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
					vowels=vowels+1
					return ''.join(random.choice(letters) for i in range(stringLength))
				
		print('0.My student number is:' , my_stNr)
		print('1.Number of primes in my student number:', count)
		print('2.Random number is: ', x)
		print('3.Number of strings to be generated: ',round(r,0))
		print('4.Random string list: *****')
		print('################')
		for i in range(0,r):
			if i%2 ==0:
				print(i,randomString(5))
				else
				
SyntaxError: invalid syntax
>>> for num in num_str:
	if num >1:
		for i in range(2, num //2):
			if num % i==0:
				break
			else:
				prime.append(num)
				count +=1
		x = random.randint(25,50)
		r=x/count
		def randomString(stringLength):
			letters = string.ascii_lowercase
			vowels=0
			for i in letters:
				if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
					vowels=vowels+1
					return ''.join(random.choice(letters) for i in range(stringLength))

		print('0.My student number is:' , my_stNr)
		print('1.Number of primes in my student number:', count)
		print('2.Random number is: ', x)
		print('3.Number of strings to be generated: ',round(r,0))
		print('4.Random string list: *****')
		print('################')
		for i in range(0,r):
			if i%2 ==0:
				print(i,randomString(5))
			else
			
SyntaxError: invalid syntax
>>> print('0.My student number is:' , my_stNr)
0.My student number is: 15128271
>>> print('1.Number of primes in my student number:', count)
1.Number of primes in my student number: 0
>>> print('2.Random number is: ', x)
2.Random number is:  35
>>> print('3.Number of strings to be generated: ',round(r,0))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print('3.Number of strings to be generated: ',round(r,0))
NameError: name 'r' is not defined
>>> print('4.Random string list: *****')
4.Random string list: *****
>>> 
