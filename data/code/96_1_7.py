class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        inner1 = a and b
        inner2 = c and not d
        result = inner1 or inner2
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_a = False
    sample_b = True
    sample_c = False
    sample_d = True
    output = evaluator.check_complex_condition(sample_a, sample_b, sample_c, sample_d)
    print(output)