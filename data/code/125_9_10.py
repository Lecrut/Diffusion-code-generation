operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

def calculate(operation, a, b):
    if operation in operations:
        return operations[operation](a, b)
    else:
        raise ValueError("Invalid operation specified")

if __name__ == '__main__':
    result_add = calculate('add', 10, 5)
    result_subtract = calculate('subtract', 10, 5)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")