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
        tokens = []
        current_token = ""
        i = 0
        while i < len(expression):
            char = expression[i]
            if char == ' ':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            elif char in '+-*/%&|^><=':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                if i + 1 < len(expression) and expression[i + 1] == char and char in '<>=':
                    tokens.append(char + char)
                    i += 1
                elif char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
                    tokens.append('**')
                    i += 1
                elif char == '<' and i + 1 < len(expression) and expression[i + 1] == '<':
                    tokens.append('<<')
                    i += 1
                elif char == '>' and i + 1 < len(expression) and expression[i + 1] == '>':
                    tokens.append('>>')
                    i += 1
                else:
                    tokens.append(char)
            else:
                current_token += char
            i += 1
        if current_token:
            tokens.append(current_token)
        
        operations = []
        for token in tokens:
            if token in self.precedence:
                operations.append({
                    'operator': token,
                    'precedence': self.get_precedence(token),
                    'associativity': self.get_associativity(token)
                })
        return operations

if __name__ == '__main__':
    parser = OperatorPrecedence()
    result = parser.parse_expression("a << b + c * d")
    print(result)