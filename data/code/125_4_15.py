operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print("Addition Result:", operations['add'](num1, num2))
    print("Subtraction Result:", operations['subtract'](num1, num2))