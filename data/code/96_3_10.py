class BooleanEvaluator:
    AND = 'and'
    OR = 'or'

    @staticmethod
    def evaluate(expression):
        if isinstance(expression, list) and len(expression) == 3:
            left = BooleanEvaluator.evaluate(expression[0])
            operator = expression[1]
            right = BooleanEvaluator.evaluate(expression[2])
            if operator == BooleanEvaluator.AND:
                return left and right
            elif operator == BooleanEvaluator.OR:
                return left or right
        else:
            return bool(expression)

if __name__ == '__main__':
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = BooleanEvaluator.evaluate(sample_expression)
    print(result)