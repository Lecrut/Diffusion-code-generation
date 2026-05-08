def evaluate_expression(expression, values):
    if not expression:
        return None
    tokens = expression.split()
    result_stack = []
    operand_stack = []
    operator_stack = []
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            operand_stack.append(float(token))
        elif token in ('AND', 'OR', 'NOT'):
            if token == 'NOT':
                if not operand_stack:
                    raise ValueError("NOT requires an operand")
                operand = operand_stack.pop()
                result = not operand
                operand_stack.append(result)
            elif token in ('AND', 'OR'):
                if len(operand_stack) < 2:
                    raise ValueError(f"{token} requires two operands")
                right = operand_stack.pop()
                left = operand_stack.pop()
                if token == 'AND':
                    result = left and right
                elif token == 'OR':
                    result = left or right
                operand_stack.append(result)
        else:
            try:
                value = float(token)
                operand_stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    if len(operand_stack) != 1:
        raise ValueError("Invalid expression structure")
    return operand_stack[0]
def test_harness():
    test_cases = [
        ("NOT 1", [1]),
        ("NOT (2 AND 3)", [2, 3]),
        ("(1 OR 2) AND 3", [1, 2, 3]),
        ("1 AND (2 OR 3)", [1, 2, 3]),
        ("NOT 1 OR 2", [1, 2]),
        ("NOT (1 AND 2) OR 3", [1, 2, 3]),
        ("1 OR (2 AND NOT 3)", [1, 2, 3]),
        ("NOT 1 AND (2 OR 3)", [1, 2, 3]),
        ("1 AND 2 AND NOT 3", [1, 2, 3]),
        ("NOT (1 OR 2) AND NOT 3", [1, 2, 3]),
    ]
    for expression, values in test_cases:
        try:
            result = evaluate_expression(expression, values)
            print(f"Expression: '{expression}' with values {values}: Result = {result}")
        except Exception as e:
            print(f"Error evaluating '{expression}' with values {values}: {e}")
        print("-" * 20)
if __name__ == '__main__':
    test_harness()