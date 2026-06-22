operations = {
    'add': lambda x, y: x + y,
}

def perform_operation(operation_name, a, b):
    return operations[operation_name](a, b)

if __name__ == '__main__':
    result = perform_operation('add', 5, 3)
    print(result)