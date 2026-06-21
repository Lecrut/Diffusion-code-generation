class BooleanEvaluator:

    def evaluate(self, expression):
        stack = []
        operators = {'&': lambda x, y: x & y, '|': lambda x, y: x | y, '^': lambda x, y: x ^ y}
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                right = stack.pop()
                left = stack.pop()
                result = operators[token](left, right)
                stack.append(result)
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = '1 & 0 | 1 ^ 0'
    result = evaluator.evaluate(expression)
    print(result)