class BooleanNegator:
    def __init__(self, value: bool):
        self._validate_value(value)
        self.value = value

    @staticmethod
    def _validate_value(value):
        if not isinstance(value, bool):
            raise ValueError("Value must be a boolean")

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original True: {negator_true.value}")
    negator_true.negate()
    print(f"Negated True: {negator_true.value}")

    negator_false = BooleanNegator(False)
    print("-" * 20)
    print(f"Original False: {negator_false.value}")
    negator_false.negate()
    print(f"Negated False: {negator_false.value}")