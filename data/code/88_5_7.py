class Validator:
    def check_states(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    validator = Validator()
    print(validator.check_states(True, True))
    print(validator.check_states(True, False))
    print(validator.check_states(False, True))
    print(validator.check_states(False, False))