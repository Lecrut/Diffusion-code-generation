class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.value)  # Output: True
    negator.negate()
    print(negator.value)  # Output: False