class OperatorPrecedence:
    def __init__(self):
        self.precedence = {
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
            '|': 'L',
            '^': 'L',
            '&': 'L',
            '<<': 'L',
            '>>': 'L',
            '+': 'L',
            '-': 'L',
            '*': 'L',
            '/': 'L',
            '//': 'L',
            '%': 'L',
            '**': 'R'
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
            if char in '+-*/%|^&<>':
                if char in '<>' and i + 1 < length and expression[i + 1] == char:
                    tokens.append(char + char)
                    i += 2
                elif char == '-' and i + 1 < length and expression[i + 1].isdigit():
                    num_str = '-'
                    i += 1
                    while i < length and expression[i].isdigit():
                        num_str += expression[i]
                        i += 1
                    tokens.append(int(num_str))
                elif char == '-' and i + 1 < length and expression[i + 1] == '.':
                    num_str = '-'
                    i += 1
                    while i < length and (expression[i].isdigit() or expression[i] == '.'):
                        num_str += expression[i]
                        i += 1
                    tokens.append(float(num_str))
                else:
                    tokens.append(char)
                    i += 1
            elif char.isdigit() or char == '.':
                num_str = ''
                while i < length and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                if '.' in num_str:
                    tokens.append(float(num_str))
                else:
                    tokens.append(int(num_str))
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def parse(self, expression):
        tokens = self.tokenize(expression)
        if not tokens:
            return []
        result = []
        output_queue = []
        operator_stack = []

        for token in tokens:
            if isinstance(token, (int, float)):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    result.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()
            elif token in self.precedence:
                while (operator_stack and
                       operator_stack[-1] != '(' and
                       operator_stack[-1] in self.precedence and
                       ((self.associativity[token] == 'L' and
                         self.precedence[token] <= self.precedence[operator_stack[-1]]) or
                        (self.associativity[token] == 'R' and
                         self.precedence[token] < self.precedence[operator_stack[-1]]))):
                    result.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                raise ValueError(f"Unknown token: {token}")

        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            result.append(op)

        return result

if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression = "2 + 3 * 4 ^ 5 & 6 | 7 << 8"
    result = parser.parse(expression)
    print(result)