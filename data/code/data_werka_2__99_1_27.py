class OperatorPrecedence:
    def __init__(self):
        self._precedence_map = {
            'or': 1,
            'and': 2,
            'not': 3,
            'shift': 4,
            'compare': 5,
            'add': 6,
            'mul': 7,
            'pow': 8
        }
        self._symbol_to_name = {
            '|': 'or',
            '^': 'xor',
            '&': 'and',
            '<<': 'shift',
            '>>': 'shift',
            '<': 'compare',
            '<=': 'compare',
            '>': 'compare',
            '>=': 'compare',
            '==': 'compare',
            '!=': 'compare',
            '+': 'add',
            '-': 'add',
            '*': 'mul',
            '//': 'mul',
            '%': 'mul',
            '**': 'pow',
            'not': 'not'
        }

    def parse_expression(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            return []
        
        precedence_values = []
        for token in tokens:
            if token in self._symbol_to_name:
                op_name = self._symbol_to_name[token]
                if op_name == 'xor':
                    prec = self._precedence_map['and'] + 1
                elif op_name == 'not':
                    prec = self._precedence_map['not']
                else:
                    prec = self._precedence_map[op_name]
                precedence_values.append((token, prec))
        
        sorted_ops = sorted(precedence_values, key=lambda x: x[1])
        return [op for op, _ in sorted_ops]

    def _tokenize(self, expression):
        tokens = []
        i = 0
        length = len(expression)
        while i < length:
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char in '0123456789':
                j = i
                while j < length and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif i + 1 < length and expression[i:i+2] in self._symbol_to_name:
                tokens.append(expression[i:i+2])
                i += 2
            elif char in self._symbol_to_name:
                tokens.append(char)
                i += 1
            else:
                i += 1
        return tokens

if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression = "10 & 5 | 20 << 1 ** 2"
    result = parser.parse_expression(expression)
    print(result)