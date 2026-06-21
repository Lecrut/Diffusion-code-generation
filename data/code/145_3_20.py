class BooleanEvaluator:

    def evaluate(self, expression):
        stack = []
        operators = set(['and', 'or'])
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == 'and':
                    stack.append(a & b)
                elif token == 'or':
                    stack.append(a | b)
        return stack[0]
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expression = '1 and 0 or 1'
    result = evaluator.evaluate(expression)
    print(result)