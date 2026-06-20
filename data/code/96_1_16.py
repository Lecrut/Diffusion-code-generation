class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        result = (a and b) or (c and not d)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_a = False
    sample_b = True
    sample_c = True
    sample_d = True
    output = evaluator.check_complex_condition(sample_a, sample_b, sample_c, sample_d)
    print(output)