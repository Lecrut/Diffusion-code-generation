class DualBooleanValidator:
    def __init__(self, first_flag: bool, second_flag: bool) -> None:
        self._validate_attribute(first_flag, "first_flag")
        self._validate_attribute(second_flag, "second_flag")
        self.first_flag = first_flag
        self.second_flag = second_flag

    def _validate_attribute(self, value: bool, name: str) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a boolean type")

    def are_both_false(self) -> bool:
        return not self.first_flag and not self.second_flag

if __name__ == '__main__':
    validator = DualBooleanValidator(False, False)
    result = validator.are_both_false()
    print(result)