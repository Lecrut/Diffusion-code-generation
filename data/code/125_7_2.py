operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

def perform_operation(operation, a, b):
    return operations[operation](a, b)

if __name__ == '__main__':
    print(perform_operation('add', 5, 3))
    print(perform_operation('subtract', 10, 4))