class BooleanValidator:
    def both_true(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    validator = BooleanValidator()
    result = validator.both_true(True, False)
    print(result)