class OperatorPrecedence:
    def __init__(self):
        self.tokens = []
        self.precedence_map = {
            '|': 1,
            '^': 2,
            '&': 3,
            '<<': 4,
            '>>': 4,
            '+': 5,
            '-': 5,
            '*': 6,
            '/': 6,
            '//': 6,
            '%': 6,
            '**': 7,
            'not': 8
        }
        self.associativity = {
            '|': 'left',
            '^': 'left',
            '&': 'left',
            '<<': 'left',
            '>>': 'left',
            '+': 'left',
            '-': 'left',
            '*': 'left',
            '/': 'left',
            '//': 'left',
            '%': 'left',
            '**': 'right',
            'not': 'right'
        }

    def tokenize(self, expression):
        self.tokens = []
        i = 0
        length = len(expression)
        while i < length:
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char == 'n' and expression[i:i+3] == 'not':
                self.tokens.append('not')
                i += 3
                continue
            if char in ['|', '^', '&', '+', '-']:
                self.tokens.append(char)
                i += 1
                continue
            if char == '<':
                if i + 1 < length and expression[i+1] == '<':
                    self.tokens.append('<<')
                    i += 2
                    continue
            if char == '>':
                if i + 1 < length and expression[i+1] == '>':
                    self.tokens.append('>>')
                    i += 2
                    continue
            if char == '*':
                if i + 1 < length and expression[i+1] == '*':
                    self.tokens.append('**')
                    i += 2
                    continue
            if char in ['/', '%']:
                self.tokens.append(char)
                i += 1
                continue
            if char.isdigit() or (char == '.' and i + 1 < length and expression[i+1].isdigit()):
                num_str = ''
                while i < length and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                self.tokens.append(num_str)
                continue
            raise ValueError(f"Unknown character: {char}")
        return self.tokens

    def get_precedence(self, op):
        if op in self.precedence_map:
            return self.precedence_map[op]
        return 0

    def get_associativity(self, op):
        return self.associativity.get(op, 'left')

    def parse(self, expression):
        self.tokenize(expression)
        result = []
        operators = []
        i = 0
        length = len(self.tokens)
        while i < length:
            token = self.tokens[i]
            if token in ['|', '^', '&', '<<', '>>', '+', '-', '*', '/', '//', '%', '**']:
                while (
                    operators
                    and operators[-1] != '('
                    and self.get_precedence(operators[-1]) > self.get_precedence(token)
                    or (
                        self.get_precedence(operators[-1]) == self.get_precedence(token)
                        and self.get_associativity(operators[-1]) == 'left'
                    )
                ):
                    result.append(operators.pop())
                operators.append(token)
                i += 1
            elif token == 'not':
                operators.append(token)
                i += 1
            elif token == '(':
                operators.append(token)
                i += 1
            elif token == ')':
                while operators and operators[-1] != '(':
                    result.append(operators.pop())
                if operators and operators[-1] == '(':
                    operators.pop()
                i += 1
            else:
                result.append(token)
                i += 1
        while operators:
            result.append(operators.pop())
        return result

if __name__ == '__main__':
    parser = OperatorPrecedence()
    print(parser.parse('1 + 2 * 3'))
    print(parser.parse('10 // 3 % 2'))