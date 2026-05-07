import re
def evaluate_simple_expression(expression):
    match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", expression)
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
    test_cases = [
        ("10 + 5", 15),
        ("20 - 8", 12),
        ("6 * 7", 42),
        ("100 / 4", 25),
        ("12 / 3", 4),
        ("50 - 15", 35),
        ("9 * 2", 18)
    ]
    for expression, expected in test_cases:
        try:
            result = evaluate_simple_expression(expression)
            assert result == expected, f"Expression: {expression}, Expected: {expected}, Got: {result}"
            print(f"PASS: {expression} = {result}")
        except Exception as e:
            print(f"FAIL: {expression} raised an exception: {e}")
    try:
        evaluate_simple_expression("10 / 0")
    except ZeroDivisionError as e:
        print("PASS: Division by zero handled correctly.")
    except Exception as e:
        print(f"FAIL: Division by zero raised unexpected error: {e}")
    try:
        evaluate_simple_expression("10 $ 5")
    except ValueError as e:
        print("PASS: Invalid operator handled correctly.")
    except Exception as e:
        print(f"FAIL: Invalid operator raised unexpected error: {e}")