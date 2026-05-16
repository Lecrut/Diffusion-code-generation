def evaluate_expression(expression, values):
    if not expression:
        return False
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    operand_stack = []
    def apply_op():
        op = operator_stack.pop()
        if len(operand_stack) < 2:
            raise ValueError("Insufficient operands for operator")
        b = operand_stack.pop()
        a = operand_stack.pop()
        if op == 'AND':
            result = a and b
        elif op == 'OR':
            result = a or b
        elif op == 'NOT':
            result = not a
        else:
            raise ValueError(f"Unknown operator: {op}")
        result_stack.append(result)
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            operand_stack.append(float(token))
        elif token in ('AND', 'OR', 'NOT'):
            operator_stack.append(token)
        else:
            try:
                value = float(token)
                if token == 'True':
                    value = True
                elif token == 'False':
                    value = False
                operand_stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
        if (token == 'True' or token == 'False') or (token.isdigit() or (token.startswith('-') and token[1:].isdigit())):
            if operator_stack and operator_stack[-1] == 'NOT':
                operand_stack.append(not operand_stack.pop())
            elif operator_stack and operator_stack[-1] in ('AND', 'OR'):
                apply_op()
                operand_stack.append(result_stack[-1])
    if operator_stack:
        while operator_stack:
            apply_op()
    if len(operand_stack) == 1 and not operator_stack:
        return operand_stack[0]
    return None
def test_nested_boolean_logic(expression, values):
    try:
        result = evaluate_expression(expression, values)
        return result
    except Exception as e:
        return f"Error: {e}"
def run_tests():
    test_cases = [
        ("NOT True AND False", [True, False], False),
        ("(True OR False) AND True", [True, False, True], True),
        ("NOT (True AND False)", [True, False], True),
        ("True OR (False AND True)", [True, False, True], True),
        ("NOT (True OR False)", [True, False], False),
        ("(False AND True) OR False", [False, True, False], False),
        ("NOT True OR False AND True", [True, False, True], False),
        ("True AND (False OR True)", [True, False, True], True),
        ("NOT (True AND True)", [True, True], False),
        ("False OR NOT False", [False, False], False)
    ]
    print("--- Running Test Harness ---")
    all_passed = True
    for i, (expr, vals, expected) in enumerate(test_cases):
        actual = test_nested_boolean_logic(expr, vals)
        status = "PASS" if actual == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"Test {i+1}: Expression: '{expr}' | Values: {vals} | Expected: {expected} | Actual: {actual} | Status: {status}")
    if all_passed:
        print("\nAll 10 tests passed successfully.")
    else:
        print("\nSome tests failed.")
if __name__ == '__main__':
    run_tests()