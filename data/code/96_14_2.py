def evaluate_nested_boolean_expression(expression):
    stack = []
    operators = []
    values = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isalnum():
            num_str = ""
            while i < len(expression) and expression[i].isalnum():
                num_str += expression[i]
                i += 1
            if num_str:
                values.append(float(num_str))
            else:
                raise ValueError("Invalid character sequence")
        elif char == '(':
            stack.append(char)
            operators.append('(')
        elif char == ')':
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            stack.pop()
            operators.pop()
        elif char in '+-*/':
            operators.append(char)
        else:
            raise ValueError(f"Invalid character in expression: {char}")
        i += 1
    if stack:
        raise ValueError("Mismatched parentheses remaining")
    if len(values) == 0:
        return False
    if len(values) == 1:
        return bool(values[0])
    if len(values) == 2:
        op = operators[0]
        if op == '(':
            raise ValueError("Invalid expression structure")
        if op in '+-*/':
            try:
                if op == '+':
                    return values[0] and values[1]
                elif op == '-':
                    return values[0] and (not values[1])
                elif op == '*':
                    return values[0] and values[1]
                elif op == '/':
                    return values[0] and (values[1] != 0) and (values[0] > values[1])
            except ZeroDivisionError:
                return False
    if len(values) > 2:
        return False
    return False
if __name__ == '__main__':
    test_cases = [
        ("((1) AND (2))", False),
        ("(True AND False)", False),
        ("((1) OR (0))", True),
        ("(1 AND 0)", False),
        ("(True OR True)", True),
        ("((1) AND (1))", True),
        ("(1 OR 0)", True),
        ("((1) AND (0))", False),
        ("((True) AND (False))", False),
        ("((1) OR (1))", True),
        ("((1) AND (1))", True),
        ("((1) OR (0))", True),
        ("((1) AND (0))", False),
        ("((True) OR (True))", True),
        ("((1) AND (1))", True),
        ("((1) OR (0))", True),
        ("((1) AND (0))", False),
        ("((True) OR (True))", True),
        ("((1) AND (1))", True),
        ("((1) OR (0))", True),
    ]
    for expression, expected in test_cases:
        try:
            result = evaluate_nested_boolean_expression(expression)
            assert result == expected, f"Expression: {expression}, Expected: {expected}, Got: {result}"
            print(f"PASS: {expression} -> {result}")
        except ValueError as e:
            print(f"ERROR: {expression} raised ValueError: {e}")
        except Exception as e:
            print(f"UNEXPECTED ERROR for {expression}: {e}")
    print("\n--- Additional Test Cases ---")
    try:
        evaluate_nested_boolean_expression("(1 AND 2")
    except ValueError as e:
        print(f"Caught expected error for '(1 AND 2': {e}")
    try:
        evaluate_nested_boolean_expression("(1 $ 2)")
    except ValueError as e:
        print(f"Caught expected error for '(1 $ 2)': {e}")
    print("Simulation complete.")