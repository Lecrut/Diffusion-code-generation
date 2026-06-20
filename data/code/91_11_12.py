class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def validate_input(self) -> None:
        if not isinstance(self.value, bool):
            raise ValueError("Input must be a boolean")

    def negate(self) -> bool:
        self.validate_input()
        self.value = not self.value
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.negate())  # Output: False