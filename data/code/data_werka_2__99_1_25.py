class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
            'or': 1,
            'xor': 2,
            'and': 3,
            'shift_left': 4,
            'shift_right': 4,
            'add': 5,
            'subtract': 5,
            'multiply': 6,
            'divide': 6,
            'floor_divide': 6,
            'modulo': 6,
            'power': 7
        }
        self.associativity = {
            'or': 'left',
            'xor': 'left',
            'and': 'left',
            'shift_left': 'left',
            'shift_right': 'left',
            'add': 'left',
            'subtract': 'left',
            'multiply': 'left',
            'divide': 'left',
            'floor_divide': 'left',
            'modulo': 'left',
            'power': 'right'
        }
        self.operator_map = {
            '|': 'or',
            '^': 'xor',
            '&': 'and',
            '<<': 'shift_left',
            '>>': 'shift_right',
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply',
            '/': 'divide',
            '//': 'floor_divide',
            '%': 'modulo',
            '**': 'power'
        }

    def parse_expression(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            return []
        output_queue = []
        operator_stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if self._is_number(token):
                output_queue.append(token)
            elif token in self.operator_map:
                op_name = self.operator_map[token]
                prec = self.precedence[op_name]
                assoc = self.associativity[op_name]
                while operator_stack:
                    top = operator_stack[-1]
                    if top in self.operator_map:
                        top_name = self.operator_map[top]
                        top_prec = self.precedence[top_name]
                        top_assoc = self.associativity[top_name]
                        if (assoc == 'left' and prec <= top_prec) or (assoc == 'right' and prec < top_prec):
                            output_queue.append(operator_stack.pop())
                        else:
                            break
                    else:
                        break
                operator_stack.append(token)
            i += 1
        while operator_stack:
            output_queue.append(operator_stack.pop())
        return output_queue

    def _tokenize(self, expression):
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
            if char in self.operator_map:
                if current:
                    tokens.append(current)
                    current = ''
                if i + 1 < len(expression) and expression[i + 1] == char and char in ['<', '>']:
                    tokens.append(char + char)
                    i += 2
                    continue
                tokens.append(char)
                i += 1
                continue
            if char.isdigit() or char == '.':
                current += char
                i += 1
                continue
            if char == '(':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append('(')
                i += 1
                continue
            if char == ')':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append(')')
                i += 1
                continue
            i += 1
        if current:
            tokens.append(current)
        return tokens

    def _is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    parser = OperatorPrecedence()
    result = parser.parse_expression('3 + 4 * 2 / ( 1 - 5 ) ** 2')
    print(result)