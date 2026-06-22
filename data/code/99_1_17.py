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
        self.left_associative = {
            'or': True,
            'and': True,
            'not': False,
            '<<': True,
            '>>': True,
            '|': True,
            '^': True,
            '&': True,
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
        tokens = self.tokenize(expression)
        precedence_list = []
        for token in tokens:
            if token in self.precedence:
                precedence_list.append(token)
        return precedence_list

    def tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char in '+-*/%':
                if char == '/' and i + 1 < len(expression) and expression[i+1] == '/':
                    tokens.append('//')
                    i += 2
                    continue
                tokens.append(char)
                i += 1
                continue
            if char == '*':
                if i + 1 < len(expression) and expression[i+1] == '*':
                    tokens.append('**')
                    i += 2
                    continue
                tokens.append(char)
                i += 1
                continue
            if char == '<':
                if i + 1 < len(expression) and expression[i+1] == '<':
                    tokens.append('<<')
                    i += 2
                    continue
                raise ValueError(f"Unsupported operator: {char}")
            if char == '>':
                if i + 1 < len(expression) and expression[i+1] == '>':
                    tokens.append('>>')
                    i += 2
                    continue
                raise ValueError(f"Unsupported operator: {char}")
            if char == '&':
                tokens.append('&')
                i += 1
                continue
            if char == '|':
                tokens.append('|')
                i += 1
                continue
            if char == '^':
                tokens.append('^')
                i += 1
                continue
            if char == 'n' and expression[i:i+3] == 'not':
                tokens.append('not')
                i += 3
                continue
            if char == 'a' and expression[i:i+3] == 'and':
                tokens.append('and')
                i += 3
                continue
            if char == 'o' and expression[i:i+2] == 'or':
                tokens.append('or')
                i += 2
                continue
            raise ValueError(f"Unexpected character: {char}")
        return tokens

if __name__ == '__main__':
    op = OperatorPrecedence()
    print(op.get_precedence('*'))
    print(op.get_precedence('/'))
    print(op.get_precedence('//'))
    print(op.get_precedence('%'))
    print(op.get_precedence('**'))
    print(op.is_left_associative('*'))
    print(op.is_left_associative('**'))
    print(op.parse_expression('a + b * c'))
    print(op.parse_expression('a ** b + c'))