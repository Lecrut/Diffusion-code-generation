def evaluate_simple_expression(expression_string):
    parts = expression_string.split()
    if len(parts) != 3:
        raise ValueError("Expression must contain exactly two numbers and one operator.")
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        raise ValueError("All parts must be valid numbers.")
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator. Must be one of +, -, *, /.")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Unknown operator.")
    return result
if __name__ == '__main__':
    test_cases = [
        ("10 + 5", 15.0),
        ("20 - 8", 12.0),
        ("6 * 7", 42.0),
        ("100 / 4", 25.0),
        ("3.5 * 2", 7.0),
        ("10 / 3", 3.3333333333333335)
    ]
    for expression, expected in test_cases:
        try:
            actual = evaluate_simple_expression(expression)
            assert abs(actual - expected) < 1e-9, f"Input: '{expression}', Expected: {expected}, Got: {actual}"
            print(f"PASS: '{expression}' -> {actual}")
        except Exception as e:
            print(f"FAIL: '{expression}' raised an exception: {e}")
    error_cases = [
        ("10 + 5 + 2", None),
        ("10 / 0", None),
        ("a + 5", None),
        ("10 $ 5", None)
    ]
    for expression in error_cases:
        try:
            evaluate_simple_expression(expression)
            print(f"FAIL: '{expression}' should have raised an error but passed.")
        except Exception as e:
            print(f"PASS: '{expression}' correctly raised an error: {e}")