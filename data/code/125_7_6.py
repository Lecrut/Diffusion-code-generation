ADDITION = 'add'
SUBTRACTION = 'subtract'

def perform_operation(operation, a, b):
    if operation == ADDITION:
        return a + b
    elif operation == SUBTRACTION:
        return a - b
    else:
        raise ValueError('Unsupported operation')
if __name__ == '__main__':
    result_add = perform_operation(ADDITION, 5, 3)
    result_subtract = perform_operation(SUBTRACTION, 10, 4)
    print('Addition Result:', result_add)
    print('Subtraction Result:', result_subtract)