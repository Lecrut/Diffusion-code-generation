class OperatorPrecedence:
    def __init__(self):
        self.precedence_map = {
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
        if operator in self.precedence_map:
            return self.precedence_map[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def get_associativity(self, operator):
        if operator in self.associativity:
            return self.associativity[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def parse_expression(self, expression):
        tokens = expression.split()
        if not tokens:
            return []
        
        operations = []
        for token in tokens:
            if token in self.precedence_map:
                operations.append({
                    'operator': token,
                    'precedence': self.get_precedence(token),
                    'associativity': self.get_associativity(token)
                })
        return operations

if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression = "x << y & z | w"
    result = parser.parse_expression(expression)
    print(result)