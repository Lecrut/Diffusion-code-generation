class BooleanEvaluator:
    def evaluate(self, expression):
        stack = []
        operators = {'&': lambda a, b: a & b, '|': lambda a, b: a | b, '^': lambda a, b: a ^ b}
        
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
        
        return stack[0]

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = "1 & 0 | 1 ^ 1"
    print(evaluator.evaluate(expression))