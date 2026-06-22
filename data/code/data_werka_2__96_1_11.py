class BooleanEvaluator:
    _TRUE_VALUE = True
    _FALSE_VALUE = False

    def check_complex_condition(self, a, b, c, d):
        if not all(isinstance(val, bool) for val in (a, b, c, d)):
            raise ValueError("All arguments must be booleans")
        if a and b:
            return self._TRUE_VALUE
        if c and not d:
            return self._TRUE_VALUE
        return self._FALSE_VALUE

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    val1 = evaluator.check_complex_condition(True, True, False, True)
    print(val1)
    val2 = evaluator.check_complex_condition(False, False, True, False)
    print(val2)