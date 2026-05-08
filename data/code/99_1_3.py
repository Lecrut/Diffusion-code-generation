import re
def evaluate_expression(expression):
    tokens = re.findall(r'(\d+\.?\d*|\+|\-|\*|\/|\(|\))', expression)
    values = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    def apply_op(op, b, a):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': 
            if b == 0: raise ZeroDivisionError
            return int(a / b) if a % b == 0 else a / b
        return None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or (token.replace('.', '', 1).isdigit()):
            values.append(float(token))
        elif token in precedence:
            op = token
            if not values:
                raise ValueError("Syntax error: Operator without preceding operand")
            if i > 0 and tokens[i-1] == '(':
                pass
            elif i > 0 and tokens[i-1] in precedence:
                while (operators and operators[-1] in precedence and 
                       precedence.get(operators[-1], 0) >= precedence[op]):
                    op_prev = operators.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    result = apply_op(op_prev, val2, val1)
                    values.append(result)
                    operators.append(op)
            operators.append(op)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                result = apply_op(op, val2, val1)
                values.append(result)
            if not operators or operators[-1] != '(':
                raise ValueError("Mismatched parentheses")
            operators.pop()
        i += 1
    while operators:
        op = operators.pop()
        val2 = values.pop()
        val1 = values.pop()
        result = apply_op(op, val2, val1)
        values.append(result)
    if len(values) != 1:
        raise ValueError("Invalid expression structure")
    return values[0]
if __name__ == '__main__':
    expressions = [
        "1 + 2 * 3",
        "(1 + 2) * 3",
        "10 / 2 + 5 * 2",
        "5 * (3 + 4) / 2",
        "10 - 5 + 2",
        "2 * (3 + (4 / 2))"
    ]
    for expr in expressions:
        try:
            result = evaluate_expression(expr)
            print(f"Expression: {expr}, Result: {result}")
        except Exception as e:
            print(f"Expression: {expr}, Error: {e}")