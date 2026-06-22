class DualBooleanValidator:
    def __init__(self, val_a: bool, val_b: bool):
        self._validate_boolean(val_a, "val_a")
        self._validate_boolean(val_b, "val_b")
        self.val_a = val_a
        self.val_b = val_b

    def _validate_boolean(self, value, name):
        if type(value) is not bool:
            raise ValueError(f"{name} must be a boolean")

    def are_both_false(self):
        return not self.val_a and not self.val_b

if __name__ == '__main__':
    instance = DualBooleanValidator(False, False)
    print(instance.are_both_false())