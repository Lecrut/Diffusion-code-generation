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
    number1 = 10
    number2 = 0
    operation = '/'
    result = evaluate_binary_operation(number1, number2, operation)
    print(result)
    number1 = 10
    number2 = 5
    operation = '*'
    result = evaluate_binary_operation(number1, number2, operation)
    print(result)
    number1 = 20
    number2 = 0
    operation = '/'
    result = evaluate_binary_operation(number1, number2, operation)
    print(result)
    number1 = 15
    number2 = 7
    operation = '-'
    result = evaluate_binary_operation(number1, number2, operation)
    print(result)