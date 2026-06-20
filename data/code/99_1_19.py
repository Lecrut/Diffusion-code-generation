class OperatorPrecedence:

    def __init__(self):
        self.precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '&': 3, '|': 4, '^': 5}

    def parse_expression(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit():
                j = i
                while j + 1 < len(expression) and (expression[j + 1].isdigit() or expression[j + 1] == '.'):
                    j += 1
                tokens.append(float(expression[i:j + 1]))
                i = j + 1
                continue
            if char in self.precedence:
                tokens.append(char)
            elif char != ' ':
                raise ValueError(f'Invalid character: {char}')
            i += 1
        return tokens

    def evaluate(self, expression):
        tokens = self.parse_expression(expression)
        values = []
        operators = []
        for token in tokens:
            if isinstance(token, float):
                values.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self.apply_op(operators, values)
                operators.pop()
            else:
                while operators and operators[-1] != '(' and (self.precedence[operators[-1]] >= self.precedence[token]):
                    self.apply_op(operators, values)
                operators.append(token)
        while operators:
            self.apply_op(operators, values)
        return values[0]

    def apply_op(self, operators, values):
        operator = operators.pop()
        b = values.pop()
        a = values.pop()
        if operator == '+':
            values.append(a + b)
        elif operator == '-':
            values.append(a - b)
        elif operator == '*':
            values.append(a * b)
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError('Division by zero')
            values.append(a / b)
        elif operator == '&':
            values.append(int(a) & int(b))
        elif operator == '|':
            values.append(int(a) | int(b))
        elif operator == '^':
            values.append(int(a) ^ int(b))
if __name__ == '__main__':
    op = OperatorPrecedence()
    print(op.evaluate('3 + 5 * (2 - 8)'))
    print(op.evaluate('10 & 4'))
    print(op.evaluate('15 | 6'))
    print(op.evaluate('7 ^ 3'))