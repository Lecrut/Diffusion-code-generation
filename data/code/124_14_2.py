OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 'Cannot divide by zero'
}

def calculate(operation, a, b):
    return OPERATIONS.get(operation, 'Invalid operation')(a, b)

if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.2
    print("Addition:", calculate('+', num1, num2))
    print("Subtraction:", calculate('-', num1, num2))
    print("Multiplication:", calculate('*', num1, num2))
    print("Division:", calculate('/', num1, num2))