class DualBooleanValidator:
    def __init__(self, value_one: bool, value_two: bool) -> None:
        self._validate_boolean(value_one, "value_one")
        self._validate_boolean(value_two, "value_two")
        self.value_one = value_one
        self.value_two = value_two

    def _validate_boolean(self, val: bool, name: str) -> None:
        if not isinstance(val, bool):
            raise ValueError(f"{name} must be a boolean")

    def are_both_false(self) -> bool:
        return self.value_one is False and self.value_two is False

if __name__ == '__main__':
    validator = DualBooleanValidator(False, False)
    print(validator.are_both_false())