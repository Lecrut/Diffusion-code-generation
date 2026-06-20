class BooleanExpressionEvaluator:
    def evaluate(self, condition_a, condition_b, condition_c):
        return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator()
    result1 = evaluator.evaluate(True, True, False)
    result2 = evaluator.evaluate(False, False, True)
    result3 = evaluator.evaluate(True, False, True)
    print(result1)
    print(result2)
    print(result3)