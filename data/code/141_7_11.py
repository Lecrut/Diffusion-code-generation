class ExpressionEvaluator:

    def __init__(self):
        self.operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y, 'NOT': lambda x: not x}

    def evaluate(self, expression):
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token in self.operators:
                right = stack.pop()
                left = stack.pop() if token != 'NOT' else None
                result = self.operators[token](left, right)
                stack.append(result)
            else:
                stack.append(token == 'True')
        return stack[0]
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate('True AND False OR True'))
    print(evaluator.evaluate('NOT True AND NOT False'))