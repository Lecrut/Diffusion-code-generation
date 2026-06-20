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
    op_symbol = '+'
    
    if op_symbol in operations:
        result = operations[op_symbol](num1, num2)
        print(result)
    else:
        print("Invalid operation symbol")

if __name__ == '__main__':
    main()