def setup_operator_precedence():
    precedence_map = {
        '(': 0,
        ')': 0,
        '==': 1,
        '!=': 1,
        '>': 2,
        '<': 2,
        '+': 3,
        '-': 3,
        '*': 4,
        '/': 4,
        'and': 5,
        'or': 6
    }
    return precedence_map
def evaluate_expression(expression, precedence_map):
    tokens = expression.split()
    result_stack = []
    operator_stack = []
    def apply_op(op, values):
        if len(values) < 2:
            raise ValueError("Insufficient operands for operator " + op)
        op2 = values.pop()
        op1 = values.pop()
        if op in precedence_map:
            precedence = precedence_map[op]
            while operator_stack and operator_stack[-1] != '(' and precedence_map.get(operator_stack[-1], 0) >= precedence:
                op = operator_stack.pop()
                values.pop()
                result_stack.append(apply_op(op, result_stack))
            operator_stack.append(op)
        else:
            result_stack.append(op1 + op2 if op == '+' else op1 - op2 if op == '-' else op1 * op2 if op == '*' else op1 if op == '/' else op1)
    for token in tokens:
        if token in precedence_map or token in '()':
            operator_stack.append(token)
        elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            result_stack.append(float(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                op = operator_stack.pop()
                values.pop()
                result_stack.append(apply_op(op, result_stack))
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        else:
            if token in precedence_map:
                apply_op(token, result_stack)
            else:
                raise ValueError(f"Unknown token: {token}")
    while operator_stack:
        op = operator_stack.pop()
        values.pop()
        result_stack.append(apply_op(op, result_stack))
    return result_stack[0] if result_stack else None
if __name__ == '__main__':
    precedence_map = setup_operator_precedence()
    expression1 = "10 + 5 * 2"
    print(f"Expression: {expression1}")
    try:
        result1 = evaluate_expression(expression1, precedence_map)
        print(f"Result: {result1}\n")
    except Exception as e:
        print(f"Error evaluating {expression1}: {e}\n")
    expression2 = "(10 + 5) * 2"
    print(f"Expression: {expression2}")
    try:
        result2 = evaluate_expression(expression2, precedence_map)
        print(f"Result: {result2}\n")
    except Exception as e:
        print(f"Error evaluating {expression2}: {e}\n")
    expression3 = "10 - 5 + 2"
    print(f"Expression: {expression3}")
    try:
        result3 = evaluate_expression(expression3, precedence_map)
        print(f"Result: {result3}\n")
    except Exception as e:
        print(f"Error evaluating {expression3}: {e}\n")
    expression4 = "10 and 5 or 3"
    print(f"Expression: {expression4}")
    try:
        result4 = evaluate_expression(expression4, precedence_map)
        print(f"Result: {result4}\n")
    except Exception as e:
        print(f"Error evaluating {expression4}: {e}\n")
    expression5 = "10 * 2 / 5"
    print(f"Expression: {expression5}")
    try:
        result5 = evaluate_expression(expression5, precedence_map)
        print(f"Result: {result5}\n")
    except Exception as e:
        print(f"Error evaluating {expression5}: {e}\n")