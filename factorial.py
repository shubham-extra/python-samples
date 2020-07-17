def factorial(num):
  a, b = 1, 0
  for _ in range(num):
    a, b = b, a+b
  return b

if __name__ == '__main__':
  for i in range(100):
    print(factorial(i))
  
