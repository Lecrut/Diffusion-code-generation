class BooleanNegator:
    def __init__(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean.")
        self.value = value

    def negate(self) -> 'BooleanNegator':
        self.value = not self.value
        return self

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original: {negator_true.value}")  # Output: True
    negated_value = negator_true.negate().value
    print(f"Negated: {negated_value}")  # Output: False