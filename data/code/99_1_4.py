import re
def evaluate_expression(expression):
    tokens = re.findall(r'(\d+\.?\d*|\(|\)|\+|-|\*|\/|\^)', expression)
    values = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def apply_op(op, b, a):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        if op == '^': return a ** b
        return None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or (token.replace('.', '', 1).isdigit()):
            num = float(token)
            values.append(num)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            operators.pop()
        elif token in precedence:
            while (operators and operators[-1] in precedence and 
                   precedence.get(operators[-1], 0) >= precedence.get(token, 0)):
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            operators.append(token)
        i += 1
    while operators:
        op = operators.pop()
        val2 = values.pop()
        val1 = values.pop()
        values.append(apply_op(op, val2, val1))
    return values[0] if values else None
if __name__ == '__main__':
    expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 / 2 + 5",
        "2^3 - 1",
        "1 + 2 * 3 / 4",
        "8 / (2 + 3) * 5",
        "10 + (2 * (6 - 4))"
    ]
    for expr in expressions:
        try:
            result = evaluate_expression(expr)
            print(f"Expression: {expr}, Result: {result}")
        except Exception as e:
            print(f"Expression: {expr}, Error: {e}")
        print("-" * 20)