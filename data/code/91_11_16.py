class BooleanNegator:
    def __init__(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        self.value = value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(negator_true.value)  # Output: True
    negator_true.negate()
    print(negator_true.value)  # Output: False

    negator_false = BooleanNegator(False)
    print(negator_false.value)  # Output: False
    negator_false.negate()
    print(negator_false.value)  # Output: True