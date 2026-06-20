class OperatorPrecedence:
    def parse_expression(self, expression):
        precedence = {
            '&': 3,
            '|': 2,
            '^': 1
        }
        stack = []
        output = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            elif expression[i] == '(':
                stack.append(expression[i])
            elif expression[i] == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       precedence.get(stack[-1], 0) >= precedence.get(expression[i], 0)):
                    output.append(stack.pop())
                stack.append(expression[i])
            i += 1
        while stack:
            output.append(stack.pop())
        return ''.join(output)

if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = "a & b | c ^ d"
    print(op.parse_expression(expression))