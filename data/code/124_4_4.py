operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else None
}

if __name__ == '__main__':
    num1 = 8
    num2 = 2
    for operation, func in operations.items():
        result = func(num1, num2)
        print(f'{operation}(8, 2) = {result}')