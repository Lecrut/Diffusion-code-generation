import re

class OperatorPrecedence:
    def __init__(self):
        self.precedence = {'&': 4, '|': 3, '<<': 2, '>>': 2, '^': 1}

    def parse_expression(self, expression):
        tokens = re.findall(r'(\d+\.?\d*|\(|\))|(&|\||<<|>>|\^)', expression)
        values = []
        ops = []

        def apply_op(op):
            right = values.pop()
            left = values.pop()
            if op == '&':
                values.append(left & right)
            elif op == '|':
                values.append(left | right)
            elif op == '<<':
                values.append(left << right)
            elif op == '>>':
                values.append(left >> right)
            elif op == '^':
                values.append(left ^ right)

        def greater_precedence(op1, op2):
            return self.precedence[op1] > self.precedence[op2]

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or (token.replace('.', '', 1).isdigit()):
                values.append(int(token))
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    apply_op(ops.pop())
                ops.pop()
            else:
                while ops and greater_precedence(ops[-1], token):
                    apply_op(ops.pop())
                ops.append(token)
            i += 1

        while ops:
            apply_op(ops.pop())

        return values[0]

if __name__ == '__main__':
    op = OperatorPrecedence()
    result = op.parse_expression('3 & 5 | 2')
    print(result)