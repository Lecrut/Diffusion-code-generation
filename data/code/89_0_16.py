def evaluate_binary_op(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            result = num1 / num2
    else:
        return "Error: Invalid operation"
    
    return result

if __name__ == '__main__':
    a = 8
    b = 3
    operation = '+'
    print(evaluate_binary_op(a, b, operation))