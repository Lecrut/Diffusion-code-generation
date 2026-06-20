class StateValidator:
    def validate_states(self, state_x: bool, state_y: bool) -> bool:
        return state_x and state_y

if __name__ == '__main__':
    validator = StateValidator()
    sample1 = validator.validate_states(True, True)
    print(f"validate_states(True, True): {sample1}")
    sample2 = validator.validate_states(False, False)
    print(f"validate_states(False, False): {sample2}")