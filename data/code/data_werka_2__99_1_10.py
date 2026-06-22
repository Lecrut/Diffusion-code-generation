class OperatorPrecedence:
    def __init__(self):
        self.precedence_levels = {
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
            '**': 7
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
            '**': 'right'
        }

    def parse_expression(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            return []
        parsed_ops = []
        precedence_stack = []
        operator_stack = []
        
        for i, token in enumerate(tokens):
            if token in self.precedence_levels:
                current_prec = self.precedence_levels[token]
                current_assoc = self.associativity[token]
                
                while operator_stack:
                    top_op = operator_stack[-1]
                    if top_op == '(':
                        break
                    top_prec = self.precedence_levels.get(top_op, 0)
                    top_assoc = self.associativity.get(top_op, 'left')
                    
                    if (current_assoc == 'left' and current_prec <= top_prec) or \
                       (current_assoc == 'right' and current_prec < top_prec):
                        parsed_ops.append(operator_stack.pop())
                    else:
                        break
                
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    parsed_ops.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")
        
        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            parsed_ops.append(op)
            
        return parsed_ops

    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char == '(' or char == ')':
                tokens.append(char)
                i += 1
            elif char in ('+', '-', '*', '/', '%', '^', '|', '&'):
                if char == '/' and i + 1 < len(expression) and expression[i+1] == '/':
                    tokens.append('//')
                    i += 2
                elif char == '*' and i + 1 < len(expression) and expression[i+1] == '*':
                    tokens.append('**')
                    i += 2
                else:
                    tokens.append(char)
                    i += 1
            elif char == '<' and i + 1 < len(expression) and expression[i+1] == '<':
                tokens.append('<<')
                i += 2
            elif char == '>' and i + 1 < len(expression) and expression[i+1] == '>':
                tokens.append('>>')
                i += 2
            else:
                raise ValueError(f"Unsupported character: {char}")
        return tokens

if __name__ == '__main__':
    op_parser = OperatorPrecedence()
    expression = "a & b | c << d ** e"
    result = op_parser.parse_expression(expression)
    print(result)