class OperatorPrecedence:
    def __init__(self):
        self.token_map = {
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
        self.left_assoc = {
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

    def _tokenize(self, expr):
        tokens = []
        i = 0
        while i < len(expr):
            char = expr[i]
            if char.isspace():
                i += 1
                continue
            if char.isdigit():
                j = i
                while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                    j += 1
                tokens.append(('NUM', expr[i:j]))
                i = j
                continue
            if char == 'n' and i + 3 < len(expr) and expr[i+1:i+4] == 'not':
                tokens.append(('OP', 'not'))
                i += 4
                continue
            if char == 'a' and i + 3 < len(expr) and expr[i+1:i+4] == 'and':
                tokens.append(('OP', 'and'))
                i += 4
                continue
            if char == 'o' and i + 2 < len(expr) and expr[i+1:i+3] == 'or':
                tokens.append(('OP', 'or'))
                i += 3
                continue
            if i + 1 < len(expr) and expr[i:i+2] in ('<<', '>>', '**'):
                tokens.append(('OP', expr[i:i+2]))
                i += 2
                continue
            if char in ('|', '^', '&', '+', '-', '*', '/', '%'):
                tokens.append(('OP', char))
                i += 1
                continue
            raise ValueError(f"Unknown character: {char}")
        return tokens

    def parse(self, expr):
        tokens = self._tokenize(expr)
        result = []
        op_stack = []
        
        for token_type, token_val in tokens:
            if token_type == 'NUM':
                result.append(token_val)
                continue
            
            if token_val == 'not':
                while op_stack and op_stack[-1] != '(':
                    result.append(op_stack.pop())
                op_stack.append(token_val)
                continue

            if token_val == '(':
                op_stack.append(token_val)
                continue
            
            if token_val == ')':
                while op_stack and op_stack[-1] != '(':
                    result.append(op_stack.pop())
                if not op_stack:
                    raise ValueError("Mismatched parentheses")
                op_stack.pop()
                continue

            while op_stack and op_stack[-1] != '(':
                prev_op = op_stack[-1]
                prev_prec = self.token_map.get(prev_op, 0)
                curr_prec = self.token_map.get(token_val, 0)
                
                if prev_prec > curr_prec:
                    result.append(op_stack.pop())
                    continue
                if prev_prec == curr_prec:
                    if not self.left_assoc.get(token_val, True):
                        break
                    result.append(op_stack.pop())
                    continue
                break
            
            op_stack.append(token_val)
        
        while op_stack:
            if op_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            result.append(op_stack.pop())
        
        return result

if __name__ == '__main__':
    parser = OperatorPrecedence()
    print(parser.parse("3 + 4 * 2"))
    print(parser.parse("(3 + 4) * 2"))
    print(parser.parse("10 ** 2"))
    print(parser.parse("not 1 and 0"))