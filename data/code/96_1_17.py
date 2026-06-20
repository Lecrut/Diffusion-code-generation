class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        if a and b:
            return True
        if c and not d:
            return True
        return False

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, False)
    print(result)