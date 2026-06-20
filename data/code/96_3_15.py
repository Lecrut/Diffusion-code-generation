class BooleanExpressionEvaluator:
    OPERATORS = {
        'and': lambda x, y: x and y,
        'or': lambda x, y: x or y
    }

    @staticmethod
    def evaluate(expression):
        if isinstance(expression, list) and len(expression) == 3:
            left = BooleanExpressionEvaluator.evaluate(expression[0])
            operator = expression[1]
            right = BooleanExpressionEvaluator.evaluate(expression[2])
            return BooleanExpressionEvaluator.OPERATORS.get(operator, lambda x, y: False)(left, right)
        else:
            return bool(expression)

if __name__ == '__main__':
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = BooleanExpressionEvaluator.evaluate(sample_expression)
    print(result)