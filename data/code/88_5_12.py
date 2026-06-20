class Validation:
    def both_true(self, state1, state2):
        return state1 and state2

if __name__ == '__main__':
    validator = Validation()
    result = validator.both_true(True, True)
    print(result)