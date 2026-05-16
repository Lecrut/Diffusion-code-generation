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
        ("15 - 3", 12),
        ("5 * 10", 50),
        ("100 / 0", "Error")                               
    ]
    for expression, expected in test_cases:
        try:
            result = evaluate_simple_expression(expression)
            print(f"Expression: '{expression}', Result: {result}, Expected: {expected}")
            assert result == expected
        except (ValueError, ZeroDivisionError) as e:
            print(f"Expression: '{expression}', Error encountered: {e}")
        except Exception as e:
            print(f"Expression: '{expression}', Unexpected Error: {e}")
        print("-" * 20)