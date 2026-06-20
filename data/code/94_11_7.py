class BooleanEvaluator:
    def is_any_true(self, data, bool_list):
        return data or any(bool_list)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.is_any_true(True, [False, False]))
    print(evaluator.is_any_true(False, [True, False]))
    print(evaluator.is_any_true(False, [False, True]))
    print(evaluator.is_any_true(False, []))