class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator1 = BooleanNegator(True)
    print(f"Initial value: {negator1.value}")  # Output: True
    negator1.negate()
    print(f"Negated value: {negator1.value}")  # Output: False

    negator2 = BooleanNegator(False)
    print(f"Initial value: {negator2.value}")  # Output: False
    negator2.negate()
    print(f"Negated value: {negator2.value}")  # Output: True