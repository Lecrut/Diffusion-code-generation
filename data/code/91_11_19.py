class BooleanNegator:
    def __init__(self, initial_value: bool):
        self.value = initial_value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.value)  # Output: True
    negator.negate()
    print(negator.value)  # Output: False