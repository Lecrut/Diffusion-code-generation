class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        if not (isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool)):
            raise ValueError("All arguments must be booleans")
        
        first_part = a and b
        if first_part:
            return True
        
        second_part = c and (not d)
        return second_part

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.check_complex_condition(True, False, True, True)
    print(result1)
    result2 = evaluator.check_complex_condition(True, True, False, False)
    print(result2)
    result3 = evaluator.check_complex_condition(False, False, True, False)
    print(result3)