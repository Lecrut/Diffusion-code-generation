class OperatorPrecedence:

    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '<<': 3, '>>': 3, '&': 4, '^': 5, '|': 6}

    def parse_expression(self, expression):
        tokens = re.findall('\\d+\\.\\d*|\\d+|\\(|\\)|\\+|-|\\*|/|<<|>>|&|\\^|\\||!', expression)
        values = []
        ops = []
        for token in tokens:
            if token.isdigit():
                values.append(int(token))
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    self.apply_op(ops, values)
                ops.pop()
            else:
                while ops and ops[-1] in self.precedence and (self.precedence[ops[-1]] >= self.precedence[token]):
                    self.apply_op(ops, values)
                ops.append(token)
        while ops:
            self.apply_op(ops, values)
        return values[0]

    def apply_op(self, ops, values):
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        if op == '+':
            values.append(a + b)
        elif op == '-':
            values.append(a - b)
        elif op == '*':
            values.append(a * b)
        elif op == '/':
            values.append(int(a / b) if a % b == 0 else a / b)
        elif op == '<<':
            values.append(a << b)
        elif op == '>>':
            values.append(a >> b)
        elif op == '&':
            values.append(a & b)
        elif op == '^':
            values.append(a ^ b)
        elif op == '|':
            values.append(a | b)
if __name__ == '__main__':
    op = OperatorPrecedence()
    print(op.parse_expression('3 + 5 * (2 - 8)'))