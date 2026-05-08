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
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') <= 1):
            values.append(float(token))
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
                   precedence.get(operators[-1], 0) >= precedence[token]):
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
    expression1 = "3 + 4 * 2"
    print(f"Expression: {expression1}, Result: {evaluate_expression(expression1)}")
    expression2 = "(3 + 4) * 2"
    print(f"Expression: {expression2}, Result: {evaluate_expression(expression2)}")
    expression3 = "10 / 2 - 3 * 4"
    print(f"Expression: {expression3}, Result: {evaluate_expression(expression3)}")
    expression4 = "8 / (2 + 3) * 5"
    print(f"Expression: {expression4}, Result: {evaluate_expression(expression4)}")
    expression5 = "10 + 2 * (6 - 3) / 2"
    print(f"Expression: {expression5}, Result: {evaluate_expression(expression5)}")
    expression6 = "1 + 2 + 3"
    print(f"Expression: {expression6}, Result: {evaluate_expression(expression6)}")