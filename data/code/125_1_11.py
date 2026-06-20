operations = {'add': lambda x, y: x + y, 'subtract': lambda x, y: x - y}

def perform_operation(operation, a, b):
    return operations[operation](a, b)
if __name__ == '__main__':
    result_add = perform_operation('add', 5, 3)
    result_subtract = perform_operation('subtract', 10, 4)
    print(result_add)
    print(result_subtract)