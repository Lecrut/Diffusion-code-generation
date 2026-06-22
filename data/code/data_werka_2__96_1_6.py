class BooleanEvaluator:
    def __init__(self):
        self._registry = {}

    def check_complex_condition(self, a, b, c, d):
        if not (isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool)):
            raise ValueError("Inputs must be boolean")
        
        term1 = a and b
        term2 = c and (not d)
        result = term1 or term2
        
        self._registry[(a, b, c, d)] = result
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    res1 = evaluator.check_complex_condition(True, True, False, False)
    print(res1)
    res2 = evaluator.check_complex_condition(False, False, True, True)
    print(res2)
    res3 = evaluator.check_complex_condition(True, False, True, True)
    print(res3)