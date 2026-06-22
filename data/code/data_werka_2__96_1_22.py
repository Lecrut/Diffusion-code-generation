TRUE_VALUE = True
FALSE_VALUE = False

class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
            raise ValueError("All inputs must be boolean values")
        
        first_part = a and b
        second_part = c and not d
        
        return first_part or second_part

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    res = evaluator.check_complex_condition(True, False, True, True)
    print(res)
    res2 = evaluator.check_complex_condition(False, False, False, False)
    print(res2)