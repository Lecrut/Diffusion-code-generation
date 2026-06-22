class BooleanEvaluator:
    _TRUE = 1
    _FALSE = 0

    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
            raise ValueError("Arguments must be boolean")
        term_a = self._TRUE if a else self._FALSE
        term_b = self._TRUE if b else self._FALSE
        term_c = self._TRUE if c else self._FALSE
        term_d = self._FALSE if d else self._TRUE
        and_part_1 = term_a & term_b
        and_part_2 = term_c & term_d
        final_value = and_part_1 | and_part_2
        return bool(final_value)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    val1 = evaluator.check_complex_condition(True, True, False, True)
    val2 = evaluator.check_complex_condition(False, False, True, False)
    val3 = evaluator.check_complex_condition(True, False, False, False)
    print(val1)
    print(val2)
    print(val3)