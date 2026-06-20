class BooleanValidator:
    def validate_states(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    validator = BooleanValidator()
    result1 = validator.validate_states(True, True)
    print(f"validate_states(True, True): {result1}")
    result2 = validator.validate_states(True, False)
    print(f"validate_states(True, False): {result2}")
    result3 = validator.validate_states(False, True)
    print(f"validate_states(False, True): {result3}")
    result4 = validator.validate_states(False, False)
    print(f"validate_states(False, False): {result4}")