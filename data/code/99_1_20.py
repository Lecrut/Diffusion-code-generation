class OperatorPrecedence:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '<<': 3, '>>': 3, '&': 4, '^': 5, '|': 6}

    def is_operator(self, token):
        return token in self.precedence

    def apply_op(self, op, b, a):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        elif op == '<<':
            return a << b
        elif op == '>>':
            return a >> b
        elif op == '&':
            return a & b
        elif op == '^':
            return a ^ b
        elif op == '|':
            return a | b

    def parse_expression(self, expression):
        tokens = re.findall(r'\d+\.?\d*|\+|-|\*|/|<<|>>|&|^|\||\(|\)', expression)
        values = []
        operators = []

        for token in tokens:
            if token.isdigit() or (token.replace('.', '', 1).isdigit()):
                values.append(float(token))
            elif self.is_operator(token):
                while (operators and
                       self.precedence[operators[-1]] >= self.precedence[token]):
                    b = values.pop()
                    a = values.pop()
                    op = operators.pop()
                    result = self.apply_op(op, b, a)
                    values.append(result)
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators[-1] != '(':
                    b = values.pop()
                    a = values.pop()
                    op = operators.pop()
                    result = self.apply_op(op, b, a)
                    values.append(result)
                operators.pop()

        while operators:
            b = values.pop()
            a = values.pop()
            op = operators.pop()
            result = self.apply_op(op, b, a)
            values.append(result)

        return values[0]

if __name__ == '__main__':
    operator_precedence = OperatorPrecedence()
    expression = "3 + 5 * (2 - 8)"
    print(operator_precedence.parse_expression(expression))