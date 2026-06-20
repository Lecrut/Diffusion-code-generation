class BooleanEvaluator:
    def check_complex_condition(self, a, b, c, d):
        intermediate_result_1 = a and b
        intermediate_result_2 = c and not d
        final_result = intermediate_result_1 or intermediate_result_2
        return final_result

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.check_complex_condition(True, False, True, False)
    print(result)