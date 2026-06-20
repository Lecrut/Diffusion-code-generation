class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original True Value: {negator_true.value}")  # Output: Original True Value: True
    negator_true.negate()
    print(f"Negated True Value: {negator_true.value}")  # Output: Negated True Value: False

    negator_false = BooleanNegator(False)
    print(f"Original False Value: {negator_false.value}")  # Output: Original False Value: False
    negator_false.negate()
    print(f"Negated False Value: {negator_false.value}")  # Output: Negated False Value: True