class BooleanEvaluator:
    _VALID_TYPES = (bool,)

    def __init__(self):
        self._cache = {}

    @staticmethod
    def _validate_inputs(a, b, c, d):
        inputs = [a, b, c, d]
        for idx, val in enumerate(inputs):
            if not isinstance(val, BooleanEvaluator._VALID_TYPES):
                raise ValueError(f"Argument at index {idx} must be a boolean, got {type(val).__name__}")

    def check_complex_condition(self, a, b, c, d):
        self._validate_inputs(a, b, c, d)
        
        key = (a, b, c, d)
        if key in self._cache:
            return self._cache[key]
        
        term_one = a and b
        term_two = c and (not d)
        result = term_one or term_two
        
        self._cache[key] = result
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    res = evaluator.check_complex_condition(True, False, True, True)
    print(res)
    res2 = evaluator.check_complex_condition(False, True, False, False)
    print(res2)