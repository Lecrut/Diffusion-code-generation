class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> None:
        self.value = not self.value

if __name__ == '__main__':
    negator_true = BooleanNegator(True)
    print(f"Original True: {negator_true.value}")
    negator_true.negate()
    print(f"Negated True: {negator_true.value}")

    negator_false = BooleanNegator(False)
    print(f"Original False: {negator_false.value}")
    negator_false.negate()
    print(f"Negated False: {negator_false.value}")