class BooleanEvaluator:
    _VALID_TYPES = (bool,)
    _LOGIC_PATTERN = "complex_nested"

    @staticmethod
    def _validate_inputs(*args):
        for arg in args:
            if type(arg) not in BooleanEvaluator._VALID_TYPES:
                raise ValueError("All arguments must be of type bool")

    @staticmethod
    def _compute_first_term(a, b):
        return a and b

    @staticmethod
    def _compute_second_term(c, d):
        return c and not d

    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        self._validate_inputs(a, b, c, d)
        term_one = self._compute_first_term(a, b)
        term_two = self._compute_second_term(c, d)
        return term_one or term_two

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, True, False, False)
    print(result)