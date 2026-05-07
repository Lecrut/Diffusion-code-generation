import sys
def evaluate_binary_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
if __name__ == '__main__':
    a = 10
    b = 5
    op = '/'
    result = evaluate_binary_operation(a, b, op)
    print(f"First number: {a}")
    print(f"Second number: {b}")
    print(f"Operation: {op}")
    print(f"Result: {result}")
    a = 10
    b = 0
    op = '/'
    result = evaluate_binary_operation(a, b, op)
    print(f"First number: {a}")
    print(f"Second number: {b}")
    print(f"Operation: {op}")
    print(f"Result: {result}")
    a = 10
    b = 5
    op = '*'
    result = evaluate_binary_operation(a, b, op)
    print(f"First number: {a}")
    print(f"Second number: {b}")
    print(f"Operation: {op}")
    print(f"Result: {result}")