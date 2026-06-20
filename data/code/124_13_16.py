operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else float('inf')
}

if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.5
    print(operations['add'](num1, num2))
    print(operations['subtract'](num1, num2))
    print(operations['multiply'](num1, num2))
    print(operations['divide'](num1, num2))