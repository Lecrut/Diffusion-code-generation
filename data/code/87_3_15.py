class ExpressionEvaluator:

    def evaluate_expression(self, condition_a: bool, condition_b: bool, condition_c: bool) -> bool:
        return condition_a and condition_b or condition_c
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    result1 = evaluator.evaluate_expression(True, False, True)
    print(result1)
    result2 = evaluator.evaluate_expression(False, False, False)
    print(result2)
    result3 = evaluator.evaluate_expression(True, True, False)
    print(result3)