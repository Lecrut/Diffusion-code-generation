class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_complex_condition(True, False, True, False))
    print(evaluator.check_complex_condition(False, False, True, True))
    print(evaluator.check_complex_condition(True, True, False, False))