class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        result = (a and b) or (c and not d)
        return result
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    result = evaluator.check_complex_condition(a_val, b_val, c_val, d_val)
    print(result)