n = int(input().strip())
condition = n % 2
if condition == 0:
   if n <=5 and n >=2:
    print('Not Weird')
   elif n<=20 and n>=6:
    print('Weird')
   elif n>20:
    print('Not Weird')
else:
    print('Weird')
