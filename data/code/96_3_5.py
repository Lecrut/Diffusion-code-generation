class BooleanEvaluator:
    def evaluate(self, expression):
        if isinstance(expression, list) and len(expression) == 3:
            left = self.evaluate(expression[0])
            operator = expression[1]
            right = self.evaluate(expression[2])
            if operator == 'and':
                return left and right
            elif operator == 'or':
                return left or right
        else:
            return bool(expression)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_expression = [[['A', 'and', 'B'], 'or', 'C'], 'and', 'D']
    result = evaluator.evaluate(sample_expression)
    print(result)