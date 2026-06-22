class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
            '<<': 1,
            '>>': 1,
            '&': 2,
            '^': 3,
            '|': 4,
            '+': 5,
            '-': 5,
            '*': 6,
            '/': 6,
            '//': 6,
            '%': 6,
            '**': 7,
            'and': 8,
            'or': 9,
            'not': 10
        }
        self.left_associative = {
            '<<': True,
            '>>': True,
            '&': True,
            '^': True,
            '|': True,
            '+': True,
            '-': True,
            '*': True,
            '/': True,
            '//': True,
            '%': True,
            '**': False,
            'and': True,
            'or': True,
            'not': False
        }

    def get_precedence(self, operator):
        if operator not in self.precedence:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.precedence[operator]

    def is_left_associative(self, operator):
        if operator not in self.left_associative:
            raise ValueError(f"Unsupported operator: {operator}")
        return self.left_associative[operator]

    def parse_expression(self, expression):
        tokens = expression.split()
        if not tokens:
            return []
        
        ops = []
        operands = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in self.precedence:
                while ops and ops[-1] in self.precedence:
                    op1 = ops[-1]
                    prec1 = self.precedence[op1]
                    prec2 = self.precedence[token]
                    if (self.is_left_associative(op1) and prec1 >= prec2) or (not self.is_left_associative(op1) and prec1 > prec2):
                        ops.pop()
                    else:
                        break
                ops.append(token)
            else:
                operands.append(token)
            i += 1
        
        while ops:
            operands.append(ops.pop())
        
        return operands

if __name__ == '__main__':
    parser = OperatorPrecedence()
    expr = "10 + 5 * 2"
    result = parser.parse_expression(expr)
    print(result)
    expr2 = "10 << 2 & 5"
    result2 = parser.parse_expression(expr2)
    print(result2)