class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
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
        self.left_associative = {
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

    def parse_expression(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            return []
        
        ops = []
        operands = []
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if token in self.precedence:
                while ops and ops[-1] != '(':
                    op = ops[-1]
                    if self._should_pop(op, token):
                        ops.pop()
                        ops.append(op)
                    else:
                        break
                ops.append(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    ops.pop()
                if ops and ops[-1] == '(':
                    ops.pop()
            else:
                operands.append(token)
            i += 1
            
        while ops:
            ops.pop()
            
        return operands

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char in '+-*/%|^&<>=!':
                if char in '<>':
                    if i + 1 < len(expression) and expression[i+1] == char:
                        tokens.append(char + char)
                        i += 2
                        continue
                if char == '=' and i + 1 < len(expression) and expression[i+1] == '=':
                    tokens.append('==')
                    i += 2
                    continue
                tokens.append(char)
                i += 1
            elif char == '*' and i + 1 < len(expression) and expression[i+1] == '*':
                tokens.append('**')
                i += 2
            elif char.isdigit() or (char == '-' and i + 1 < len(expression) and expression[i+1].isdigit()):
                j = i
                if char == '-':
                    j += 1
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                i += 1
        return tokens

    def _should_pop(self, top_op, new_op):
        if top_op == '(':
            return False
        if new_op == '(':
            return False
        if top_op == '**' and new_op == '**':
            return False
        if new_op == '**':
            return False
        return self.precedence.get(top_op, 0) >= self.precedence.get(new_op, 0)

if __name__ == '__main__':
    parser = OperatorPrecedence()
    result = parser.parse_expression("3 + 4 * 2")
    print(result)
    result = parser.parse_expression("2 ** 3 ** 2")
    print(result)
    result = parser.parse_expression("(1 + 2) * 3")
    print(result)
    result = parser.parse_expression("10 % 3")
    print(result)
    result = parser.parse_expression("15 // 4")
    print(result)
    result = parser.parse_expression("2 & 3 | 4")
    print(result)
    result = parser.parse_expression("1 << 2 + 3")
    print(result)
    result = parser.parse_expression("10 / 3")
    print(result)