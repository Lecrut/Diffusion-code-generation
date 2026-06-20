def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def main():
    num1 = 10
    num2 = 5
    op = '+'
    
    if op in operations:
        result = operations[op](num1, num2)
        print(result)
    else:
        print("Invalid operation")

if __name__ == '__main__':
    main()