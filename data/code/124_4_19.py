operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else float('inf')
}

if __name__ == '__main__':
    num1 = 8
    num2 = 2
    for op in operations:
        print(operations[op](num1, num2))