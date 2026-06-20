operations = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b
}

def perform_operation(operation, a, b):
    if operation in operations:
        return operations[operation](a, b)
    else:
        raise ValueError("Invalid operation specified")

if __name__ == '__main__':
    result_add = perform_operation('add', 10, 5)
    result_subtract = perform_operation('subtract', 10, 5)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")