ADD = '+'
SUBTRACT = '-'
MULTIPLY = '*'
DIVIDE = '/'

def perform_operation(operation, a, b):
    if operation == ADD:
        return a + b
    elif operation == SUBTRACT:
        return a - b
    elif operation == MULTIPLY:
        return a * b
    elif operation == DIVIDE:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")

if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.2
    print(f"Addition: {perform_operation(ADD, num1, num2)}")
    print(f"Subtraction: {perform_operation(SUBTRACT, num1, num2)}")
    print(f"Multiplication: {perform_operation(MULTIPLY, num1, num2)}")
    try:
        print(f"Division: {perform_operation(DIVIDE, num1, num2)}")
    except ValueError as e:
        print(e)