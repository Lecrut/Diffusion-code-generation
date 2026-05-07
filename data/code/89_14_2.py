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
def main():
    num1 = 20
    num2 = 5
    symbol = '*'
    try:
        result = calculator(num1, num2, symbol)
        print(f"Result of {num1} {symbol} {num2}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()