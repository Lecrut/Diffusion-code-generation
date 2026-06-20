class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        intermediate_result_1 = self._validate_and(a, b)
        intermediate_result_2 = self._validate_and(c, not d)
        final_result = self._validate_or(intermediate_result_1, intermediate_result_2)
        return final_result
    
    def _validate_and(self, x, y):
        if isinstance(x, bool) and isinstance(y, bool):
            return x and y
        raise ValueError("Both inputs must be boolean")
    
    def _validate_or(self, x, y):
        if isinstance(x, bool) and isinstance(y, bool):
            return x or y
        raise ValueError("Both inputs must be boolean")

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, False)
    print(result)