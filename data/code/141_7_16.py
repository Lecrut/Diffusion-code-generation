class LogicalExpressionEvaluator:

    def __init__(self):
        self.operators = {'AND': lambda x, y: x and y, 'OR': lambda x, y: x or y, 'NOT': lambda x: not x}

    def evaluate(self, expression):
        stack = []
        operators = set(self.operators.keys())
        tokens = expression.split()
        for token in tokens:
            if token.isalpha() and token.upper() in operators:
                while stack and self.get_precedence(stack[-1]) >= self.get_precedence(token):
                    right = stack.pop()
                    operator = stack.pop()
                    left = stack.pop()
                    result = self.operators[operator](left, right)
                    stack.append(result)
                stack.append(token)
            else:
                stack.append(bool(int(token)))
        while len(stack) > 1:
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            result = self.operators[operator](left, right)
            stack.append(result)
        return stack[0]

    def get_precedence(self, operator):
        if operator == 'NOT':
            return 3
        elif operator in ('AND', 'OR'):
            return 2
        else:
            return 1
if __name__ == '__main__':
    evaluator = LogicalExpressionEvaluator()
    expression = 'NOT (1 AND 0 OR 1)'
    result = evaluator.evaluate(expression)
    print(result)