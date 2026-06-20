class OperatorPrecedence:
    def parse_expression(self, expression):
        precedence = {
            '&': 3,
            '|': 2,
            '^': 1
        }
        stack_ops = []
        output = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            elif expression[i] == '(':
                stack_ops.append(expression[i])
            elif expression[i] == ')':
                while stack_ops and stack_ops[-1] != '(':
                    output.append(stack_ops.pop())
                stack_ops.pop()
            else:
                while (stack_ops and stack_ops[-1] != '(' and
                       precedence[expression[i]] <= precedence.get(stack_ops[-1], 0)):
                    output.append(stack_ops.pop())
                stack_ops.append(expression[i])
            i += 1
        while stack_ops:
            output.append(stack_ops.pop())
        return ''.join(output)

if __name__ == '__main__':
    op = OperatorPrecedence()
    expression = "a & b | c ^ d"
    print(op.parse_expression(expression))