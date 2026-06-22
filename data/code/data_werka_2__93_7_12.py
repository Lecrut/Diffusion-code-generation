class DualStateValidator:
    def __init__(self, val_a: bool, val_b: bool):
        if not isinstance(val_a, bool) or not isinstance(val_b, bool):
            raise ValueError("Arguments must be boolean")
        self.a = val_a
        self.b = val_b

    def is_neither_active(self) -> bool:
        return not self.a and not self.b

    def is_any_active(self) -> bool:
        return self.a or self.b

if __name__ == '__main__':
    validator = DualStateValidator(False, False)
    print(validator.is_neither_active())
    print(validator.is_any_active())
    
    validator2 = DualStateValidator(True, False)
    print(validator2.is_neither_active())
    print(validator2.is_any_active())