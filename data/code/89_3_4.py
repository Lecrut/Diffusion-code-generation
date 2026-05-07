import re
def evaluate_simple_expression(expression):
    match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", expression.strip())
    if not match:
        raise ValueError("Invalid expression format")
    num1 = int(match.group(1))
    operator = match.group(2)
    num2 = int(match.group(3))
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 // num2
    else:
        raise ValueError("Unsupported operator")
if __name__ == '__main__':
    expressions = [
        "10 + 5",
        "20 - 8",
        "6 * 7",
        "100 / 4",
        "15 - 3",
        "50 / 10"
    ]
    for expr in expressions:
        try:
            result = evaluate_simple_expression(expr)
            print(f"Expression: {expr}, Result: {result}")
        except Exception as e:
            print(f"Error evaluating {expr}: {e}")