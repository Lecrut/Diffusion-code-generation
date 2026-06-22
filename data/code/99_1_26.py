class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
            'or': 1,
            'and': 2,
            'not': 3,
            '|': 4,
            '^': 5,
            '&': 6,
            '<<': 7,
            '>>': 7,
            '+': 8,
            '-': 8,
            '*': 9,
            '/': 9,
            '//': 9,
            '%': 9,
            '**': 10
        }
        self.left_associative = {
            'or': True,
            'and': True,
            'not': False,
            '|': True,
            '^': True,
            '&': True,
            '<<': True,
            '>>': True,
            '+': True,
            '-': True,
            '*': True,
            '/': True,
            '//': True,
            '%': True,
            '**': False
        }

    def get_precedence(self, operator):
        if operator in self.precedence:
            return self.precedence[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def is_left_associative(self, operator):
        if operator in self.left_associative:
            return self.left_associative[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def parse_expression(self, expression):
        tokens = expression.split()
        operations = []
        for token in tokens:
            if token in self.precedence:
                operations.append(token)
        return operations

if __name__ == '__main__':
    op = OperatorPrecedence()
    expr = "10 | 5 & 3 << 2"
    result = op.parse_expression(expr)
    print(result)