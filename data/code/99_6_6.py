def setup_operator_precedence():
    precedence = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        'not': 3,
        'and': 4,
        'or': 5
    }
    return precedence
def evaluate_expression(expression, precedence_map):
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    def apply_op(op, values):
        if len(values) < 2:
            raise ValueError("Insufficient operands for operator " + op)
        op2 = values.pop()
        op1 = values.pop()
        if op in ('+', '-', '*', '/', '^'):
            if op == '+':
                result = op1 + op2
            elif op == '-':
                result = op1 - op2
            elif op == '*':
                result = op1 * op2
            elif op == '/':
                result = op1 / op2
            elif op == '^':
                result = op1 ** op2
            else:
                raise ValueError("Unknown arithmetic operation: " + op)
            values.append(result)
        else:
            raise ValueError("Unknown operator: " + op)
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            result_stack.append(float(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                op = operator_stack.pop()
                apply_op(op, result_stack)
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        elif token in precedence_map:
            current_precedence = precedence_map[token]
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence_map.get(operator_stack[-1], 0) >= current_precedence):
                op = operator_stack.pop()
                apply_op(op, result_stack)
            operator_stack.append(token)
        else:
            raise ValueError("Invalid token encountered: " + token)
    while operator_stack:
        op = operator_stack.pop()
        apply_op(op, result_stack)
    return result_stack[0] if result_stack else None
if __name__ == '__main__':
    precedence_map = setup_operator_precedence()
    expression1 = "10 + 5 * 2"
    print(f"Expression: {expression1}")
    try:
        result1 = evaluate_expression(expression1, precedence_map)
        print(f"Result: {result1}\n")
    except ValueError as e:
        print(f"Error evaluating {expression1}: {e}\n")
    expression2 = "(10 + 5) * 2"
    print(f"Expression: {expression2}")
    try:
        result2 = evaluate_expression(expression2, precedence_map)
        print(f"Result: {result2}\n")
    except ValueError as e:
        print(f"Error evaluating {expression2}: {e}\n")
    expression3 = "10 - 5 + 2"
    print(f"Expression: {expression3}")
    try:
        result3 = evaluate_expression(expression3, precedence_map)
        print(f"Result: {result3}\n")
    except ValueError as e:
        print(f"Error evaluating {expression3}: {e}\n")
    expression4 = "10 and 5 or 2"
    print(f"Expression: {expression4}")
    try:
        print("Note: Boolean logic evaluation is structural, not arithmetic.")
        print(f"Structure check: 'and' (4) vs 'or' (5). 'or' should bind less tightly.")
        result4 = evaluate_expression(expression4, precedence_map)
        print(f"Result (Arithmetic context): {result4}\n")
    except ValueError as e:
        print(f"Error evaluating {expression4}: {e}\n")