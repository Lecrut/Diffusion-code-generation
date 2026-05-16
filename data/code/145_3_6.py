def evaluate_expression(expression, values):
    if not expression:
        return False
    tokens = expression.split()
    result_stack = []
    for token in tokens:
        if token == 'NOT':
            if len(result_stack) < 1:
                raise ValueError("Insufficient operands for NOT")
            operand = result_stack.pop()
            result_stack.append(not operand)
        elif token in ('AND', 'OR'):
            if len(result_stack) < 2:
                raise ValueError(f"Insufficient operands for {token}")
            op2 = result_stack.pop()
            op1 = result_stack.pop()
            if token == 'AND':
                result_stack.append(op1 and op2)
            elif token == 'OR':
                result_stack.append(op1 or op2)
        else:
            try:
                value = float(token)
                result_stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    if len(result_stack) != 1:
        raise ValueError("Invalid expression structure")
    return result_stack[0]
def run_test_case(expression, values, expected):
    try:
        result = evaluate_expression(expression, values)
        assert result == expected, f"Expression: '{expression}', Values: {values}, Expected: {expected}, Got: {result}"
        return True
    except Exception as e:
        print(f"Test Failed for '{expression}' with values {values}: Error: {e}")
        return False
if __name__ == '__main__':
    test_cases = [
        ("NOT 1 AND 0", [1, 0], False),
        ("NOT 1 OR 0", [1, 0], True),
        ("NOT 1 AND NOT 0", [1, 0], False),
        ("1 OR NOT 0", [1, 0], True),
        ("NOT 1 AND NOT 0 AND 1", [1, 0, 1], False),
        ("1 OR 0 OR NOT 1", [1, 0, 1], True),
        ("NOT 1 AND (0 OR 1)", [1, 0, 1], False),
        ("NOT (1 AND 0)", [1, 0], True),
        ("NOT (1 OR 0)", [1, 0], False),
        ("NOT (NOT 1 AND 0)", [1, 0], True)
    ]
    all_passed = True
    for i, (expression, values, expected) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        print(f"Expression: {expression}, Values: {values}, Expected: {expected}")
        if run_test_case(expression, values, expected):
            print("Result: PASSED\n")
        else:
            print("Result: FAILED\n")
            all_passed = False
        print("-" * 20 + "\n")
    if all_passed:
        print("All 10 test cases passed successfully.")
    else:
        print("Some test cases failed.")