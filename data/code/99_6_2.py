import operator
precedence = {
    '==': 1,
    '!=': 1,
    '>': 2,
    '<': 2,
    '>=': 3,
    '<=': 3,
    '&&': 4,
    '||': 4
}
def evaluate_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        return None
    result_stack = []
    operator_stack = []
    def apply_op(op, b, a):
        if op == '==':
            return a == b
        elif op == '!=':
            return a != b
        elif op == '>':
            return a > b
        elif op == '<':
            return a < b
        elif op == '>=':
            return a >= b
        elif op == '<=':
            return a <= b
        elif op == '&&':
            return a and b
        elif op == '||':
            return a or b
        return None
    for token in tokens:
        if token in values:
            result_stack.append(values[token])
        elif token in precedence:
            while (operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                op = operator_stack.pop()
                val2 = result_stack.pop()
                val1 = result_stack.pop()
                result_stack.append(apply_op(op, val2, val1))
            operator_stack.append(token)
        else:
            try:
                result_stack.append(float(token))
            except ValueError:
                pass
    while operator_stack:
        op = operator_stack.pop()
        val2 = result_stack.pop()
        val1 = result_stack.pop()
        result_stack.append(apply_op(op, val2, val1))
    if len(result_stack) == 1:
        return result_stack[0]
    return None
if __name__ == '__main__':
    sample_expression = "5 > 3 && 10 == 10 || 2 < 1"
    sample_values = {
        '5': 5,
        '3': 3,
        '10': 10,
        '2': 2,
        '1': 1
    }
    result = evaluate_expression(sample_expression, sample_values)
    print(f"Expression: {sample_expression}")
    print(f"Values: {sample_values}")
    print(f"Result: {result}")