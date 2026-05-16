def calculator(num1, num2, symbol):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    if symbol in operations:
        return operations[symbol](num1, num2)
    else:
        raise ValueError(f"Unsupported operation: {symbol}")
if __name__ == '__main__':
    a = 20
    b = 5
    op = '*'
    result = calculator(a, b, op)
    print(f"Result of {a} {op} {b}: {result}")
    a = 100
    b = 15
    op = '/'
    result = calculator(a, b, op)
    print(f"Result of {a} {op} {b}: {result}")
    a = 42
    b = 7
    op = '-'
    result = calculator(a, b, op)
    print(f"Result of {a} {op} {b}: {result}")
    try:
        calculator(10, 2, '%')
    except ValueError as e:
        print(f"Error caught: {e}")