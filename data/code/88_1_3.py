class BooleanEvaluator:
    @staticmethod
    def are_conditions_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(f"are_conditions_true(True, True): {BooleanEvaluator.are_conditions_true(True, True)}")
    print(f"are_conditions_true(True, False): {BooleanEvaluator.are_conditions_true(True, False)}")
    print(f"are_conditions_true(False, True): {BooleanEvaluator.are_conditions_true(False, True)}")
    print(f"are_conditions_true(False, False): {BooleanEvaluator.are_conditions_true(False, False)}")