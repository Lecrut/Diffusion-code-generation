import re
def evaluate_simple_expression(expression):
    match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", expression)
    if not match:
        raise ValueError("Invalid expression format")
    num1 = int(match.group(1))
    operator = match.group(2)
    num2 = int(match.group(3))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        result = num1 // num2
    else:
        raise ValueError("Unsupported operator")
    return result
if __name__ == '__main__':
    expression1 = "10 + 5"
    expression2 = "20 - 8"
    expression3 = "6 * 7"
    expression4 = "100 / 4"
    expression5 = "50 / 0"
    expression6 = "12 / 3"
    print(f"Expression: '{expression1}', Result: {evaluate_simple_expression(expression1)}")
    print(f"Expression: '{expression2}', Result: {evaluate_simple_expression(expression2)}")
    print(f"Expression: '{expression3}', Result: {evaluate_simple_expression(expression3)}")
    print(f"Expression: '{expression4}', Result: {evaluate_simple_expression(expression4)}")
    try:
        print(f"Expression: '{expression5}', Result: {evaluate_simple_expression(expression5)}")
    except ZeroDivisionError as e:
        print(f"Expression: '{expression5}', Error: {e}")
    print(f"Expression: '{expression6}', Result: {evaluate_simple_expression(expression6)}")