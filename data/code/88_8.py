class Validator:
    def are_both_true(self, a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    validator = Validator()
    print(validator.are_both_true(True, True))
    print(validator.are_both_true(True, False))
    print(validator.are_both_true(False, True))
    print(validator.are_both_true(False, False))