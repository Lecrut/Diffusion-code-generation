class BooleanEvaluator:

    def __init__(self):
        self._operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y, 'NOT': lambda x: not x}

    def evaluate(self, expression: str) -> bool:
        tokens = expression.split()
        if len(tokens) % 2 == 0 or not all((token in ('AND', 'OR', 'NOT', 'True', 'False') for token in tokens)):
            raise ValueError('Invalid input')
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token) != 0)
            elif token == 'NOT':
                if not stack:
                    raise ValueError('NOT requires an operand')
                operand = stack.pop()
                stack.append(self._operators[token](operand))
            else:
                if len(stack) < 2:
                    raise ValueError('Insufficient operands for operator')
                b = stack.pop()
                a = stack.pop()
                stack.append(self._operators[token](a, b))
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.evaluate('True AND False OR NOT True'))