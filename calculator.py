def add(n, m):
  return n + m

def sub(n, m):
  return n - m

def mul(n, m):
  return n * m

def div(n, m):
  return n / m

def mod(n, m):
  return n % m

def pow(n, m):
  return n**m

def floor_div(n, m):
  return n // m

print("Choose the method of calculation : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7. Floor Division")

choice = int(input("Please Enter Your Choice : "))

n = int(input("Enter 1st number : "))
m = int(input("Enter 2nd number : "))

if choice == 1:
  print(add(n, m))
elif choice == 2:
  print(sub(n, m))
elif choice == 3:
  print(mul(n, m))
elif choice == 4:
  print(div(n, m))
elif choice == 5:
  print(mod(n, m))
elif choice == 6:
  print(pow(n, m))
elif choice == 7:
  print(floor_div(n, m))
else:
  print("Invalid choice")
