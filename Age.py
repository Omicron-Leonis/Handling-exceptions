def enterage(age):

#define function to take input as a natural number
  if age < 0: #condtion 1
    raise ValueError("Only positive integers are allowed")
  if age %2 == 0: #condition2
   print("age is even")
  else:
    print("age is odd")

  try:
   num = int(input("Enter your age: "))
   enterage(num)

#handles value error exception
  except ValueError:
   print("Only positive integers are allowed")
  except: 
   print("Something is wrong")

