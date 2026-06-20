OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 'Cannot divide by zero'
}

def calculate(operation, a, b):
    return OPERATIONS.get(operation, 'Invalid operation')(a, b)

if __name__ == '__main__':
    NUM1 = 10.5
    NUM2 = 3.2
    print(f"Addition: {calculate('+', NUM1, NUM2)}")
    print(f"Subtraction: {calculate('-', NUM1, NUM2)}")
    print(f"Multiplication: {calculate('*', NUM1, NUM2)}")
    print(f"Division: {calculate('/', NUM1, NUM2)}")