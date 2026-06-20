class StateValidator:

    def are_both_true(self, state1: bool, state2: bool) -> bool:
        return state1 and state2
if __name__ == '__main__':
    validator = StateValidator()
    print(validator.are_both_true(True, True))
    print(validator.are_both_true(False, True))