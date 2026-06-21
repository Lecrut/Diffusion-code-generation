class BooleanExpressionEvaluator:

    def __init__(self):
        self.operators = {'AND': lambda a, b: a and b, 'OR': lambda a, b: a or b}

    def validate_expression(self, expression):
        if not expression:
            raise ValueError('Empty expression')
        tokens = expression.split()
        if len(tokens) % 2 == 0:
            raise ValueError('Invalid number of tokens')

    def evaluate(self, expression):
        self.validate_expression(expression)
        tokens = expression.split()
        operand_stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                operand_stack.append(int(token))
            elif token in self.operators:
                if len(operand_stack) < 2:
                    raise ValueError('Insufficient operands')
                b = operand_stack.pop()
                a = operand_stack.pop()
                result = self.operators[token](a, b)
                operand_stack.append(result)
        return operand_stack[0]
if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    expression = '1 AND 0 OR 1'
    result = evaluator.evaluate(expression)
    print(result)