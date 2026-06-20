class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.check_complex_condition(True, False, True, False)
    result2 = evaluator.check_complex_condition(False, True, False, True)
    print(result1)
    print(result2)