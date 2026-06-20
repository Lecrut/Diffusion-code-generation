class BooleanValidator:
    def is_true(self, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return value

    def both_true(self, state1: bool, state2: bool) -> bool:
        return self.is_true(state1) and self.is_true(state2)

if __name__ == '__main__':
    validator = BooleanValidator()
    result = validator.both_true(True, False)
    print(result)