class Validation:
    def both_true(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

if __name__ == '__main__':
    validator = Validation()
    result = validator.both_true(True, True)
    print(result)