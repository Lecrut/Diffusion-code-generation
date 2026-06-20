class ExpressionEvaluator:

    @staticmethod
    def evaluate_expression(a, b, c, d):
        return a and b or (c and (not d))
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate_expression(True, False, True, False))
    print(evaluator.evaluate_expression(False, True, False, True))