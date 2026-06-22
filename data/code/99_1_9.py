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
        self.left_associative = {
            '|': True,
            '^': True,
            '&': True,
            '<<': True,
            '>>': True,
            '+': True,
            '-': True,
            '*': True,
            '/': True,
            '//': True,
            '%': True,
            '**': False
        }

    def parse(self, expression):
        tokens = self.tokenize(expression)
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token in self.precedence:
                while (operator_stack and
                       operator_stack[-1] != '(' and
                       self.precedence.get(operator_stack[-1], 0) >= self.precedence[token] and
                       (self.left_associative[token] or self.precedence[operator_stack[-1]] > self.precedence[token])):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()
            else:
                output_queue.append(token)

        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(op)

        return output_queue

    def tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char in self.precedence:
                tokens.append(char)
                i += 1
            elif char == '(':
                tokens.append('(')
                i += 1
            elif char == ')':
                tokens.append(')')
                i += 1
            elif char.isdigit() or char == '.':
                num_str = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                tokens.append(num_str)
            else:
                raise ValueError(f"Unsupported character: {char}")
        return tokens

if __name__ == '__main__':
    parser = OperatorPrecedence()
    result = parser.parse("2 + 3 * 4")
    print(result)
    result2 = parser.parse("(2 + 3) * 4")
    print(result2)
    result3 = parser.parse("2 ** 3 ** 2")
    print(result3)
    result4 = parser.parse("2 & 3 | 4")
    print(result4)