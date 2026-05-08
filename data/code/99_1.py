import re
def evaluate_expression(expression):
    tokens = re.findall(r'(\d+\.?\d*|\+|\-|\*|\/|\(|\))', expression)
    values = []
    ops = []
    def apply_op(op, b, a):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        return None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or (token.replace('.', '', 1).isdigit()):
            values.append(float(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops[-1] != '(':
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            ops.pop()
        elif token in ('+', '-', '*', '/'):
            while (ops and ops[-1] in ('+', '-', '*', '/')) and (len(values) >= 2):
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_op(op, val2, val1))
            ops.append(token)
        i += 1
    while ops:
        op = ops.pop()
        val2 = values.pop()
        val1 = values.pop()
        values.append(apply_op(op, val2, val1))
    return values[0] if values else None
if __name__ == '__main__':
    expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 / 2 + 5 * 3",
        "8 / (2 + 3) * 5",
        "1 + 2 + 3 * 4",
        "10 - 5 / 2",
        "2 * (3 + 4) / (1 - 5)",
        "10 + 2 * (6 - 4)"
    ]
    for expr in expressions:
        try:
            result = evaluate_expression(expr)
            print(f"Expression: {expr} = {result}")
        except ZeroDivisionError as e:
            print(f"Expression: {expr} = Error: {e}")
        except Exception as e:
            print(f"Expression: {expr} = Error: {e}")