class BooleanEvaluator:
    def is_any_true(self, data, bool_list):
        return data or any(bool_list)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.is_any_true(True, [False, False])
    result2 = evaluator.is_any_true(False, [True, False])
    result3 = evaluator.is_any_true(False, [False, True])
    result4 = evaluator.is_any_true(False, [])
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Result 3: {result3}")
    print(f"Result 4: {result4}")