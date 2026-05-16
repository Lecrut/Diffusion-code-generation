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
    expression1 = "3 + 4 * 2"
    result1 = evaluate_expression(expression1)
    print(f"Expression: {expression1}, Result: {result1}")
    expression2 = "(3 + 4) * 2"
    result2 = evaluate_expression(expression2)
    print(f"Expression: {expression2}, Result: {result2}")
    expression3 = "10 / 2 - 3 * 4"
    result3 = evaluate_expression(expression3)
    print(f"Expression: {expression3}, Result: {result3}")
    expression4 = "1 + 2 + 3 * 4 / 2"
    result4 = evaluate_expression(expression4)
    print(f"Expression: {expression4}, Result: {result4}")
    expression5 = "8 / (2 - 1) * 5"
    result5 = evaluate_expression(expression5)
    print(f"Expression: {expression5}, Result: {result5}")
    expression6 = "100 / (5 * (2 + 3))"
    result6 = evaluate_expression(expression6)
    print(f"Expression: {expression6}, Result: {result6}")