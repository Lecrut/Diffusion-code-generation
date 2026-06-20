ADDITION = "addition"
SUBTRACTION = "subtraction"

def perform_operation(a, b, operation=ADDITION):
    if operation == ADDITION:
        return a + b
    elif operation == SUBTRACTION:
        return a - b
    else:
        raise ValueError("Unsupported operation")

if __name__ == '__main__':
    result_add = perform_operation(5, 3)
    result_subtract = perform_operation(10, 4)
    print(result_add)
    print(result_subtract)