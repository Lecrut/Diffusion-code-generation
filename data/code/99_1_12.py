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
        if operator not in self.precedence_map:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.precedence_map[operator]

    def get_associativity(self, operator):
        if operator not in self.associativity:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.associativity[operator]

    def parse_expression(self, expression):
        tokens = self._tokenize(expression)
        precedence_list = []
        for token in tokens:
            if token in self.precedence_map:
                precedence_list.append({
                    'operator': token,
                    'precedence': self.get_precedence(token),
                    'associativity': self.get_associativity(token)
                })
        return precedence_list

    def _tokenize(self, expression):
        operators = ['**', '<<', '>>', '|', '^', '&', '+', '-', '*', '/', '//', '%', 'or', 'and', 'not']
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char.isdigit() or char == '.':
                num_str = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                tokens.append(num_str)
                continue
            found = False
            for op in operators:
                if expression[i:i+len(op)] == op:
                    tokens.append(op)
                    i += len(op)
                    found = True
                    break
            if not found:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = "10 | 5 & 3 ** 2"
    result = op.parse_expression(expression)
    print(result)