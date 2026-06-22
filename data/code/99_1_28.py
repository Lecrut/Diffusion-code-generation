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

    def get_precedence(self, op):
        if op in self.precedence:
            return self.precedence[op]
        raise ValueError(f"Unsupported operator: {op}")

    def get_associativity(self, op):
        if op in self.left_associative:
            return self.left_associative[op]
        raise ValueError(f"Unsupported operator: {op}")

    def parse_expression(self, expression):
        tokens = expression.split()
        if not tokens:
            return []
        
        ops = []
        for token in tokens:
            if token in self.precedence:
                ops.append(token)
        
        result = []
        while ops:
            current_op = ops.pop(0)
            current_prec = self.get_precedence(current_op)
            current_assoc = self.get_associativity(current_op)
            
            if not result:
                result.append(current_op)
            else:
                last_op = result[-1]
                last_prec = self.get_precedence(last_op)
                last_assoc = self.get_associativity(last_op)
                
                if current_prec > last_prec:
                    result.append(current_op)
                elif current_prec == last_prec:
                    if current_assoc:
                        result.append(current_op)
                    else:
                        result.pop()
                        result.append(current_op)
                else:
                    result.append(current_op)
        
        return result

if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = "a + b * c >> d & e ^ f | g"
    result = op.parse_expression(expression)
    print(result)