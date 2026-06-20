class BooleanEvaluator:
    @staticmethod
    def both_false(a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    result1 = BooleanEvaluator.both_false(False, False)
    print(f"False, False -> {result1}")
    result2 = BooleanEvaluator.both_false(True, False)
    print(f"True, False -> {result2}")
    result3 = BooleanEvaluator.both_false(True, True)
    print(f"True, True -> {result3}")
    result4 = BooleanEvaluator.both_false(False, True)
    print(f"False, True -> {result4}")