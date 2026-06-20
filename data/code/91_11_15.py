class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> 'BooleanNegator':
        self.value = not self.value
        return self

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original True: {negator_true.value}")  # Output: Original True: True
    negated_negator_true = negator_true.negate()
    print(f"Negated True: {negated_negator_true.value}")  # Output: Negated True: False

    negator_false = BooleanNegator(False)
    print(f"Original False: {negator_false.value}")  # Output: Original False: False
    negated_negator_false = negator_false.negate()
    print(f"Negated False: {negated_negator_false.value}")  # Output: Negated False: True