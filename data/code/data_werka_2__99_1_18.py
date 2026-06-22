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

    def tokenize(self, expression):
        tokens = []
        i = 0
        length = len(expression)
        while i < length:
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char.isdigit() or (char == '.' and i + 1 < length and expression[i + 1].isdigit()):
                j = i
                while j < length and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(('NUM', expression[i:j]))
                i = j
                continue
            if char == 'n' and i + 3 < length and expression[i:i+4] == 'not ':
                tokens.append(('OP', 'not'))
                i += 4
                continue
            if char == 'a' and i + 3 < length and expression[i:i+4] == 'and ':
                tokens.append(('OP', 'and'))
                i += 4
                continue
            if char == 'o' and i + 2 < length and expression[i:i+3] == 'or ':
                tokens.append(('OP', 'or'))
                i += 3
                continue
            if char == 'x' and i + 3 < length and expression[i:i+4] == 'xor ':
                tokens.append(('OP', 'xor'))
                i += 4
                continue
            if char in self.operators:
                tokens.append(('OP', char))
                i += 1
                continue
            raise ValueError(f"Unknown character: {char}")
        return tokens

    def get_precedence(self, op):
        if op not in self.operators:
            raise ValueError(f"Unknown operator: {op}")
        return self.operators[op]

    def get_associativity(self, op):
        if op not in self.left_assoc:
            raise ValueError(f"Unknown operator: {op}")
        return self.left_assoc[op]

    def parse_expression(self, expression):
        tokens = self.tokenize(expression)
        if not tokens:
            return []
        
        result = []
        op_stack = []
        
        for token in tokens:
            type_, value = token
            if type_ == 'NUM':
                result.append(value)
            elif type_ == 'OP':
                while op_stack and op_stack[-1] != '(':
                    top_op = op_stack[-1]
                    if self.get_precedence(top_op) > self.get_precedence(value):
                        result.append(op_stack.pop())
                    elif self.get_precedence(top_op) == self.get_precedence(value):
                        if self.get_associativity(top_op):
                            result.append(op_stack.pop())
                        else:
                            break
                    else:
                        break
                op_stack.append(value)
        
        while op_stack:
            result.append(op_stack.pop())
        
        return result

if __name__ == '__main__':
    parser = OperatorPrecedence()
    print(parser.parse_expression("3 + 4 * 2"))
    print(parser.parse_expression("3 ** 4"))
    print(parser.parse_expression("10 / 2 + 5"))
    print(parser.parse_expression("2 + 3 * 4 ** 2"))
    print(parser.parse_expression("10 % 3 + 2"))
    print(parser.parse_expression("1 << 2 + 3"))
    print(parser.parse_expression("10 & 5 | 2"))