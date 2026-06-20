class ExpressionEvaluator:

    def evaluate(self, expression):
        if not isinstance(expression, str) or not all((char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&|~' for char in expression)):
            raise ValueError('Invalid expression')
        stack = []
        operators = {'&': lambda a, b: a and b, '|': lambda a, b: a or b, '~': lambda a: not a}

        def precedence(op):
            if op == '&':
                return 1
            elif op == '|':
                return 0
            elif op == '~':
                return 2
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isalpha():
                stack.append(char)
            elif char in operators:
                while stack and stack[-1] != '(' and (precedence(stack[-1]) >= precedence(char)):
                    right = stack.pop()
                    left = stack.pop()
                    op = stack.pop()
                    result = operators[op](left, right)
                    stack.append(result)
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    right = stack.pop()
                    left = stack.pop()
                    op = stack.pop()
                    result = operators[op](left, right)
                    stack.append(result)
                stack.pop()
            i += 1
        while len(stack) > 1:
            right = stack.pop()
            left = stack.pop()
            op = stack.pop()
            result = operators[op](left, right)
            stack.append(result)
        return stack[0]
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    expression = 'A&~B|C'
    result = evaluator.evaluate(expression)
    print(result)