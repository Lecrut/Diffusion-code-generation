def evaluate_expression(expression):
    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError("Invalid expression format")
    
    num1, operator, num2 = tokens
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Both operands must be numbers")
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Division by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

if __name__ == '__main__':
    result = evaluate_expression("10 + 5")
    print(result)