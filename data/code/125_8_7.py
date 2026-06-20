def perform_operations():
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y
    }
    num1 = 5
    num2 = 3
    result_add = operations['add'](num1, num2)
    result_subtract = operations['subtract'](num1, num2)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")

if __name__ == '__main__':
    perform_operations()