def evaluate_expression(expression, values):
    if not expression:
        return False
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    operand_stack = []
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            operand_stack.append(float(token))
        elif token in ('AND', 'OR', 'NOT'):
            if token == 'NOT':
                if not operand_stack:
                    raise ValueError("NOT requires an operand")
                operand = operand_stack.pop()
                result_stack.append(not operand)
            elif token in ('AND', 'OR'):
                if len(operand_stack) < 2:
                    raise ValueError(f"{token} requires two operands")
                right = operand_stack.pop()
                left = operand_stack.pop()
                if token == 'AND':
                    result_stack.append(left and right)
                elif token == 'OR':
                    result_stack.append(left or right)
        else:
            try:
                value = float(token)
                operand_stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    if len(operand_stack) != 1:
        raise ValueError("Malformed expression")
    final_result = operand_stack[0]
    if result_stack:
        pass 
    return final_result
def test_logic(expression, a, b, c):
    try:
        result = evaluate_expression(expression, [a, b, c])
        return result
    except Exception as e:
        return f"ERROR: {e}"
if __name__ == '__main__':
    test_cases = [
        ("NOT (1 AND 0)", 1, 0, 0),
        ("(1 AND 0) OR 1", 1, 0, 1),
        ("NOT (1 OR 0)", 1, 0, 0),
        ("(1 OR 0) AND (1 OR 0)", 1, 0, 1),
        ("NOT (1 AND 1)", 1, 1, 0),
        ("(0 OR 1) AND (0 OR 1)", 0, 1, 1),
        ("NOT (0 AND 0)", 0, 0, 1),
        ("(1 AND 1) OR (0 AND 0)", 1, 1, 0),
        ("NOT (1 OR 1)", 1, 1, 0),
        ("(1 AND 0) OR (0 AND 1)", 1, 0, 1)
    ]
    print("--- Test Harness Results ---")
    all_passed = True
    for i, (expr, a, b, c) in enumerate(test_cases):
        result = test_logic(expr, a, b, c)
        expected = None
        if i == 0: expected = False
        elif i == 1: expected = True
        elif i == 2: expected = False
        elif i == 3: expected = True
        elif i == 4: expected = False
        elif i == 5: expected = True
        elif i == 6: expected = True
        elif i == 7: expected = True
        elif i == 8: expected = False
        elif i == 9: expected = True
        if result == expected:
            status = "PASS"
        else:
            status = f"FAIL (Expected: {expected}, Got: {result})"
            all_passed = False
        print(f"Test {i+1}: Expression: '{expr}' with a={a}, b={b}, c={c} -> {status}")
    if all_passed:
        print("\nAll test cases passed successfully.")
    else:
        print("\nSome test cases failed.")