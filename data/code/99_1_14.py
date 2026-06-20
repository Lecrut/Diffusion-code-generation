class OperatorPrecedence:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '&': 2, '|': 2, '^': 3}

    def parse_expression(self, expression):
        tokens = re.findall(r'\d+\.?\d*|\+|-|&|\||\^|\(|\)', expression)
        values = []
        ops = []

        def apply_op(op, b, a):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '&':
                return a & b
            elif op == '|':
                return a | b
            elif op == '^':
                return a ^ b

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or (token.replace('.', '', 1).isdigit()):
                values.append(float(token))
            elif token in ('+', '-', '&', '|', '^', '(', ')'):
                while ops and self.precedence[ops[-1]] >= self.precedence[token]:
                    b = values.pop()
                    a = values.pop()
                    op = ops.pop()
                    values.append(apply_op(op, b, a))
                ops.append(token)
            i += 1

        while ops:
            b = values.pop()
            a = values.pop()
            op = ops.pop()
            values.append(apply_op(op, b, a))

        return values[0]

if __name__ == '__main__':
    operator_precedence = OperatorPrecedence()
    expression = "3 + 5 * (2 & 4) | 1 ^ 2"
    result = operator_precedence.parse_expression(expression)
    print(result)