class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        result = (a and b) or (c and not d)
        return result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_values = {
        'a': True,
        'b': False,
        'c': True,
        'd': False
    }
    final_result = evaluator.check_complex_condition(**sample_values)
    print(final_result)