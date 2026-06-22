class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
            'or': 1,
            'and': 2,
            'not': 3,
            '<<': 4,
            '>>': 4,
            '|': 5,
            '^': 6,
            '&': 7,
            '+': 8,
            '-': 8,
            '*': 9,
            '/': 9,
            '//': 9,
            '%': 9,
            '**': 10
        }
        self.associativity = {
            'or': 'left',
            'and': 'left',
            'not': 'right',
            '<<': 'left',
            '>>': 'left',
            '|': 'left',
            '^': 'left',
            '&': 'left',
            '+': 'left',
            '-': 'left',
            '*': 'left',
            '/': 'left',
            '//': 'left',
            '%': 'left',
            '**': 'right'
        }

    def get_precedence(self, operator):
        if operator not in self.precedence:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.precedence[operator]

    def get_associativity(self, operator):
        if operator not in self.associativity:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.associativity[operator]

    def parse_expression(self, expression):
        tokens = expression.split()
        operations = []
        for token in tokens:
            if token in self.precedence:
                operations.append(token)
        return operations

if __name__ == '__main__':
    op = OperatorPrecedence()
    expr = "10 & 5 >> 2"
    result = op.parse_expression(expr)
    print(result)
    print(op.get_precedence('&'))
    print(op.get_associativity('>>'))