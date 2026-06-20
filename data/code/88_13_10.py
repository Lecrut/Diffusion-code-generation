class BooleanEvaluator:
    TRUE = True

    @staticmethod
    def are_strictly_true(a, b):
        return bool(a) and bool(b)

if __name__ == '__main__':
    condition_1 = True
    condition_2 = False
    result = BooleanEvaluator.are_strictly_true(condition_1, condition_2)
    print(result)