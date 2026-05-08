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
    expr1 = "3 + 4 * 2"
    print(f"Expression: {expr1}, Result: {evaluate_expression(expr1)}")
    expr2 = "(3 + 4) * 2"
    print(f"Expression: {expr2}, Result: {evaluate_expression(expr2)}")
    expr3 = "10 / 2 + 3 * 5"
    print(f"Expression: {expr3}, Result: {evaluate_expression(expr3)}")
    expr4 = "10 + 2 * (6 - 3)"
    print(f"Expression: {expr4}, Result: {evaluate_expression(expr4)}")
    expr5 = "100 / (5 + 5)"
    print(f"Expression: {expr5}, Result: {evaluate_expression(expr5)}")
    expr6 = "1 + 2 + 3 * 4"
    print(f"Expression: {expr6}, Result: {evaluate_expression(expr6)}")