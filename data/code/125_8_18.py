operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

def perform_operation(operation_name, num1, num2):
    if operation_name in operations:
        return operations[operation_name](num1, num2)
    else:
        raise ValueError(f"Invalid operation: {operation_name}")

if __name__ == '__main__':
    try:
        result_add = perform_operation('add', 5, 3)
        result_subtract = perform_operation('subtract', 10, 4)
        print(f"Addition: {result_add}")
        print(f"Subtraction: {result_subtract}")
    except ValueError as e:
        print(e)