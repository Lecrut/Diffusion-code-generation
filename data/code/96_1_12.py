class BooleanEvaluator:
    _TRUE_VAL = True
    _FALSE_VAL = False
    _LOGIC_CONSTANTS = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3
    }

    @staticmethod
    def _validate_inputs(a, b, c, d):
        required_types = (bool, int)
        if not isinstance(a, required_types) or not isinstance(b, required_types):
            raise ValueError("Inputs a and b must be boolean-like")
        if not isinstance(c, required_types) or not isinstance(d, required_types):
            raise ValueError("Inputs c and d must be boolean-like")
        return bool(a), bool(b), bool(c), bool(d)

    def check_complex_condition(self, a, b, c, d):
        a, b, c, d = self._validate_inputs(a, b, c, d)
        first_term = a and b
        second_term = c and (not d)
        return first_term or second_term

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    val1 = evaluator.check_complex_condition(True, True, False, False)
    print(val1)
    val2 = evaluator.check_complex_condition(False, False, True, True)
    print(val2)
    val3 = evaluator.check_complex_condition(True, False, True, True)
    print(val3)