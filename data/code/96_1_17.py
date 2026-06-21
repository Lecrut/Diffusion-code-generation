class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        if not all(isinstance(arg, bool) for arg in [a, b, c, d]):
            raise ValueError("All inputs must be boolean values")
        return (a and b) or (c and not d)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, True)
    print(result)