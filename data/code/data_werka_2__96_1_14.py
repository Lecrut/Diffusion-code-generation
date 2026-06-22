class BooleanEvaluator:
    _TRUE_CONST = True
    _FALSE_CONST = False

    def check_complex_condition(self, a, b, c, d):
        if not (
            isinstance(a, bool) and
            isinstance(b, bool) and
            isinstance(c, bool) and
            isinstance(d, bool)
        ):
            raise ValueError("All inputs must be boolean")

        ab_term = a and b
        cd_term = c and (not d)
        final_result = ab_term or cd_term
        return final_result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    out = evaluator.check_complex_condition(False, True, False, False)
    print(out)