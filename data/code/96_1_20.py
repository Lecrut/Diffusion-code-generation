class BooleanEvaluator:
    PRIORITY_CONDITION = 2
    STANDARD_CONDITION = 1

    def check_complex_condition(self, a, b, c, d):
        if not self._are_all_boolean(a, b, c, d):
            raise ValueError("Inputs must be boolean")
        
        if self._evaluate_priority(a, b, c, d):
            return True
        
        return self._evaluate_standard(c, d)

    def _are_all_boolean(self, a, b, c, d):
        return isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool)

    def _evaluate_priority(self, a, b, c, d):
        if a and b:
            return True
        if c and not d:
            return False
        return False

    def _evaluate_standard(self, c, d):
        return c and not d

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.check_complex_condition(False, False, True, False)
    print(result1)
    result2 = evaluator.check_complex_condition(False, False, True, True)
    print(result2)
    result3 = evaluator.check_complex_condition(True, True, False, True)
    print(result3)