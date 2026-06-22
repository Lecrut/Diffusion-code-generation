class DualStateValidator:
    def __init__(self, val_a: bool, val_b: bool) -> None:
        if not isinstance(val_a, bool):
            raise ValueError("val_a must be boolean")
        if not isinstance(val_b, bool):
            raise ValueError("val_b must be boolean")
        self._first = val_a
        self._second = val_b

    def is_either_true(self) -> bool:
        return self._first or self._second

    def verify_both_false(self) -> bool:
        return not self.is_either_true()

if __name__ == '__main__':
    validator = DualStateValidator(False, False)
    result = validator.verify_both_false()
    print(result)