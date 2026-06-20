class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        inner_and_1 = a and b
        inner_and_2 = c and not d
        final_result = inner_and_1 or inner_and_2
        return final_result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(False, True, False, True)
    print(result)