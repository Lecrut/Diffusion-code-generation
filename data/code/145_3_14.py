class BooleanEvaluator:
    def __init__(self):
        self.ops = {
            'AND': lambda a, b: a & b,
            'OR': lambda a, b: a | b,
            'NOT': lambda a: ~a
        }

    def evaluate(self, expression):
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            elif token in self.ops:
                b = stack.pop()
                a = stack.pop()
                result = self.ops[token](a, b)
                stack.append(result)
        return stack[0]

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = "1 AND 0 OR 1"
    print(evaluator.evaluate(expression))