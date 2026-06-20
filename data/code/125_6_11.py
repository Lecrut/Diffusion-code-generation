operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

def perform_operation(operation_name, a, b):
    return operations.get(operation_name, lambda x, y: None)(a, b)

if __name__ == '__main__':
    print(perform_operation('add', 10, 5))
    print(perform_operation('subtract', 20, 8))