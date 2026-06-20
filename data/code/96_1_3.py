class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, False)
    print(result)