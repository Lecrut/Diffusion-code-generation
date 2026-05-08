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
            raise ValueError("Syntax error: insufficient operands")
        op2 = values.pop()
        op1 = values.pop()
        if op in precedence_map:
            result = None
            if op == '+':
                result = op1 + op2
            elif op == '-':
                result = op1 - op2
            elif op == '*':
                result = op1 * op2
            elif op == '/':
                result = op1 / op2
            elif op == '==':
                result = 1 if op1 == op2 else 0
            elif op == '!=':
                result = 1 if op1 != op2 else 0
            elif op == '>':
                result = 1 if op1 > op2 else 0
            elif op == '<':
                result = 1 if op1 < op2 else 0
            elif op == 'and':
                result = 1 if op1 and op2 else 0
            elif op == 'or':
                result = 1 if op1 or op2 else 0
            else:
                raise ValueError(f"Unknown operator: {op}")
            values.append(result)
            return
        else:
            raise ValueError(f"Unknown operator: {op}")
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            values = [float(token)]
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                apply_op(operator_stack.pop(), values)
            if not operator_stack or operator_stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            operator_stack.pop()
        elif token in precedence_map:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence_map.get(operator_stack[-1], 0) >= precedence_map[token]):
                apply_op(operator_stack.pop(), values)
            operator_stack.append(token)
        else:
            raise ValueError(f"Invalid token: {token}")
    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        apply_op(operator_stack.pop(), values)
    if len(values) != 1:
        raise ValueError("Invalid expression structure")
    return values[0]
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
    expression3 = "20 > 10 and 5 < 3"
    print(f"Expression: {expression3}")
    try:
        result3 = evaluate_expression(expression3, precedence_map)
        print(f"Result: {result3}\n")
    except ValueError as e:
        print(f"Error evaluating {expression3}: {e}\n")
    expression4 = "5 + 3 * (8 - 2) / 4"
    print(f"Expression: {expression4}")
    try:
        result4 = evaluate_expression(expression4, precedence_map)
        print(f"Result: {result4}\n")
    except ValueError as e:
        print(f"Error evaluating {expression4}: {e}\n")