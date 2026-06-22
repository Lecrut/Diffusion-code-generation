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
        if operator in self.precedence:
            return self.precedence[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def get_associativity(self, operator):
        if operator in self.associativity:
            return self.associativity[operator]
        raise ValueError(f"Unsupported operator: {operator}")

    def parse_expression(self, expression):
        tokens = expression.split()
        if not tokens:
            return []
        
        result = []
        operator_stack = []
        
        for token in tokens:
            if token in self.precedence:
                while operator_stack:
                    top = operator_stack[-1]
                    if top in self.precedence:
                        top_prec = self.get_precedence(top)
                        curr_prec = self.get_precedence(token)
                        
                        if (self.get_associativity(top) == 'left' and top_prec >= curr_prec) or \
                           (self.get_associativity(top) == 'right' and top_prec > curr_prec):
                            result.append(operator_stack.pop())
                        else:
                            break
                    else:
                        break
                operator_stack.append(token)
            else:
                result.append(token)
        
        while operator_stack:
            result.append(operator_stack.pop())
            
        return result

if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = "a + b * c"
    result = op.parse_expression(expression)
    print(result)
    
    expression2 = "a ** b * c"
    result2 = op.parse_expression(expression2)
    print(result2)
    
    expression3 = "a & b | c"
    result3 = op.parse_expression(expression3)
    print(result3)