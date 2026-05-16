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
        op2 = operand_stack.pop()
        op1 = operand_stack.pop()
        if op == 'AND':
            result = op1 and op2
        elif op == 'OR':
            result = op1 or op2
        elif op == 'NOT':
            result = not op1
        else:
            raise ValueError(f"Unknown operator: {op}")
        operand_stack.append(result)
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
            pass
        elif token in ('AND', 'OR', 'NOT'):
            if not operand_stack:
                raise ValueError("Syntax error: Operator without operands")
            if token == 'NOT':
                if len(operand_stack) < 1:
                    raise ValueError("Syntax error: NOT without operand")
                operand = operand_stack.pop()
                result = not operand
                operand_stack.append(result)
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                if token == 'AND':
                    result = operand1 and operand2
                elif token == 'OR':
                    result = operand1 or operand2
                operand_stack.append(result)
        else:
            pass
    if len(operand_stack) != 1:
        raise ValueError("Invalid expression structure")
    return operand_stack[0]
def test_nested_boolean_logic():
    test_cases = [
        (
            "NOT (A AND B) OR C", 
            {"A": True, "B": False, "C": True}, 
            True
        ),
        (
            "(A OR B) AND NOT C", 
            {"A": True, "B": True, "C": False}, 
            True
        ),
        (
            "NOT (A AND B AND C)", 
            {"A": True, "B": True, "C": True}, 
            False
        ),
        (
            "A AND (B OR NOT C)", 
            {"A": False, "B": True, "C": True}, 
            False
        ),
        (
            "NOT A OR (B AND C)", 
            {"A": True, "B": False, "C": False}, 
            True
        ),
        (
            "(NOT A OR B) AND (NOT C OR D)", 
            {"A": True, "B": True, "C": True, "D": False}, 
            False
        ),
        (
            "A OR (NOT B AND C)", 
            {"A": True, "B": False, "C": True}, 
            True
        ),
        (
            "NOT (A OR B) AND NOT (C OR D)", 
            {"A": True, "B": True, "C": False, "D": False}, 
            True
        ),
        (
            "A AND (B OR (NOT C OR D))", 
            {"A": True, "B": True, "C": False, "D": False}, 
            True
        ),
        (
            "NOT (A AND B) OR (NOT C AND D)", 
            {"A": True, "B": True, "C": True, "D": False}, 
            True
        )
    ]
    print("--- Running Test Harness ---")
    all_passed = True
    for i, (expression, values, expected) in enumerate(test_cases):
        try:
            actual = evaluate_expression(expression, values)
            if actual == expected:
                status = "PASS"
            else:
                status = f"FAIL (Expected: {expected}, Got: {actual})"
                all_passed = False
            print(f"Test Case {i+1}: Expression: '{expression}'")
            print(f"  Values: {values}")
            print(f"  Result: {actual} | Status: {status}\n")
        except Exception as e:
            print(f"Test Case {i+1}: Expression: '{expression}'")
            print(f"  Values: {values}")
            print(f"  ERROR: Evaluation failed with exception: {e}\n")
            all_passed = False
    if all_passed:
        print("--- All 10 Test Cases Passed Successfully ---")
    else:
        print("--- Some Test Cases Failed ---")
if __name__ == '__main__':
    test_nested_boolean_logic()