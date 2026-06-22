class OperatorPrecedence:
    def __init__(self):
        self.operators = {
            'or': 1,
            'xor': 2,
            'and': 3,
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
        self.left_assoc = {
            'or': True,
            'xor': True,
            'and': True,
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

    def parse(self, expression):
        tokens = []
        current = ''
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                if current:
                    tokens.append(current)
                    current = ''
                i += 1
                continue
            if char in '+-*/%|^&<>=!':
                if current:
                    tokens.append(current)
                    current = ''
                if char == '<' and i + 1 < len(expression) and expression[i + 1] == '<':
                    tokens.append('<<')
                    i += 2
                    continue
                if char == '>' and i + 1 < len(expression) and expression[i + 1] == '>':
                    tokens.append('>>')
                    i += 2
                    continue
                if char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
                    tokens.append('**')
                    i += 2
                    continue
                if char == '/' and i + 1 < len(expression) and expression[i + 1] == '/':
                    tokens.append('//')
                    i += 2
                    continue
                if char == '=' and i + 1 < len(expression) and expression[i + 1] == '=':
                    tokens.append('==')
                    i += 2
                    continue
                tokens.append(char)
                i += 1
                continue
            if char in '()':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append(char)
                i += 1
                continue
            if char.isdigit() or (char == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
                current += char
                i += 1
                continue
            if char.isalpha() or char == '_':
                current += char
                i += 1
                continue
            raise ValueError(f"Unexpected character: {char}")
        if current:
            tokens.append(current)
        return self._shunting_yard(tokens)

    def _shunting_yard(self, tokens):
        output = []
        op_stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or (token.startswith('-') and token[1:].replace('.', '').isdigit()):
                output.append(token)
            elif token in self.operators:
                prec = self.operators[token]
                while op_stack and op_stack[-1] != '(':
                    top = op_stack[-1]
                    if top in self.operators:
                        top_prec = self.operators[top]
                        if (prec < top_prec) or (prec == top_prec and self.left_assoc.get(token, True)):
                            output.append(op_stack.pop())
                            continue
                    break
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                if op_stack and op_stack[-1] == '(':
                    op_stack.pop()
            i += 1
        while op_stack:
            output.append(op_stack.pop())
        return output

if __name__ == '__main__':
    parser = OperatorPrecedence()
    result = parser.parse('3 + 4 * 2 / ( 1 - 5 ) ** 2')
    print(result)