class ExpressionEvaluator:
    SUPPORTED_OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero'
    }

    @staticmethod
    def is_valid_operator(operator):
        return operator in ExpressionEvaluator.SUPPORTED_OPERATORS

    def evaluate(self, operand1, operator, operand2):
        if not self.is_valid_operator(operator):
            raise ValueError(f'Invalid operator: {operator}')
        return ExpressionEvaluator.SUPPORTED_OPERATORS[operator](operand1, operand2)

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate(10, '+', 5))
    print(evaluator.evaluate(10, '-', 5))
    print(evaluator.evaluate(10, '*', 5))
    try:
        print(evaluator.evaluate(10, '/', 0))
    except ValueError as e:
        print(e)