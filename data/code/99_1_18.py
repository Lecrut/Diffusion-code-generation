class OperatorPrecedence:

    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '&': 3, '|': 3, '^': 3}

    def parse_expression(self, expression):
        tokens = re.findall('(\\d+\\.?\\d*|\\+|-|\\*|/|\\(|\\)|&|\\||^)', expression)
        values = []
        ops = []

        def apply_op(op):
            while ops and self.precedence[op] <= self.precedence[ops[-1]]:
                b = values.pop()
                a = values.pop()
                op2 = ops.pop()
                result = self.apply_operation(op2, a, b)
                values.append(result)
            ops.append(op)

        def finish():
            while ops:
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                result = self.apply_operation(op, a, b)
                values.append(result)
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or token.replace('.', '', 1).isdigit():
                values.append(float(token))
            elif token in self.precedence:
                apply_op(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops[-1] != '(':
                    finish()
                ops.pop()
            i += 1
        while ops:
            finish()
        return values[0]

    def apply_operation(self, op, a, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError('Division by zero')
            return a / b
        if op == '&':
            return a & b
        if op == '|':
            return a | b
        if op == '^':
            return a ^ b
if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = '3 + 5 * (2 - 8)'
    result = op.parse_expression(expression)
    print(result)