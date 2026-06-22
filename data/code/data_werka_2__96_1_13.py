TRUE_CONST = True
FALSE_CONST = False

class BooleanEvaluator:
    def __init__(self):
        self.logic_cache = {}

    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
            raise ValueError("Inputs must be boolean")
        first_part = a and b
        second_part = c and (not d)
        final_result = first_part or second_part
        self.logic_cache[(a, b, c, d)] = final_result
        return final_result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    val1 = evaluator.check_complex_condition(TRUE_CONST, FALSE_CONST, TRUE_CONST, TRUE_CONST)
    print(val1)
    val2 = evaluator.check_complex_condition(FALSE_CONST, TRUE_CONST, TRUE_CONST, FALSE_CONST)
    print(val2)
    val3 = evaluator.check_complex_condition(TRUE_CONST, TRUE_CONST, FALSE_CONST, FALSE_CONST)
    print(val3)