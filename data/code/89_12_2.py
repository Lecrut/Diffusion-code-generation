def calculate_expression(num1, num2, operator):
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
    num_a = 10
    num_b = 5
    op_symbol = '*'
    result = calculate_expression(num_a, num_b, op_symbol)
    print(f"Result: {result}")