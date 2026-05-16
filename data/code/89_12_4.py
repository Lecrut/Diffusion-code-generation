def calculate_expression(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
if __name__ == '__main__':
    num1 = 10
    operator = '*'
    num2 = 5
    result = calculate_expression(num1, operator, num2)
    print(f"Result: {result}")