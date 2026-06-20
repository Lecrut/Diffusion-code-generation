class BooleanValidator:
    def validate_inputs(self, state1: bool, state2: bool) -> None:
        if not isinstance(state1, bool):
            raise ValueError("state1 must be a boolean")
        if not isinstance(state2, bool):
            raise ValueError("state2 must be a boolean")

    def both_true(self, state1: bool, state2: bool) -> bool:
        self.validate_inputs(state1, state2)
        return state1 and state2

if __name__ == '__main__':
    validator = BooleanValidator()
    result1 = validator.both_true(True, True)
    print(f"both_true(True, True): {result1}")
    result2 = validator.both_true(True, False)
    print(f"both_true(True, False): {result2}")
    result3 = validator.both_true(False, True)
    print(f"both_true(False, True): {result3}")
    result4 = validator.both_true(False, False)
    print(f"both_true(False, False): {result4}")