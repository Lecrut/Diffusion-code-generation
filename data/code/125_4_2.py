operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print(operations['add'](num1, num2))
    print(operations['subtract'](num1, num2))