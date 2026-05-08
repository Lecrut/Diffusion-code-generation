def evaluate_expression(expression, values):
    if not expression:
        return False
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    operand_stack = []
    def apply_op():
        op = operator_stack.pop()
        if op == 'AND':
            b = operand_stack.pop()
            a = operand_stack.pop()
            result_stack.append(a and b)
        elif op == 'OR':
            b = operand_stack.pop()
            a = operand_stack.pop()
            result_stack.append(a or b)
        elif op == 'NOT':
            b = operand_stack.pop()
            result_stack.append(not b)
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            operand_stack.append(float(token))
        elif token in ('AND', 'OR', 'NOT'):
            operator_stack.append(token)
        else:
            if token in ('True', 'False'):
                operand_stack.append(token == 'True')
            else:
                raise ValueError(f"Unknown token: {token}")
    while operator_stack:
        apply_op()
    if operand_stack:
        raise ValueError("Expression parsing error: Unused operands remaining.")
    return result_stack[0] if result_stack else False
def test_harness(expression, values):
    expected = None
    try:
        result = evaluate_expression(expression, values)
        print(f"Expression: {expression}, Values: {values} -> Result: {result}")
        if expected is not None and result != expected:
            print(f"FAIL: Expected {expected}, got {result}")
            return False
        return True
    except Exception as e:
        print(f"ERROR evaluating {expression} with {values}: {e}")
        return False
if __name__ == '__main__':
    test_cases = [
        ("NOT True AND False", [True, False], False),
        ("(True OR False) AND True", [True, False, True], True),
        ("NOT (True AND False)", [True, False], True),
        ("True OR False AND True", [True, False, True], True),
        ("NOT True OR False", [True, False], False),
        ("False AND True OR False", [False, True, False], False),
        ("NOT (False OR False)", [False, False], True),
        ("True AND True AND True", [True, True, True], True),
        ("NOT False AND True", [False, True], True),
        ("False OR NOT True", [False, True], False)
    ]
    all_passed = True
    for expression, values, expected in test_cases:
        print("-" * 30)
        if not test_harness(expression, values):
            all_passed = False
    if all_passed:
        print("\nAll 10 test cases passed successfully.")
    else:
        print("\nSome test cases failed.")