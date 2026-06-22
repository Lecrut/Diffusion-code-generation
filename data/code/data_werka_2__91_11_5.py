class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> bool:
        self.value = not self.value
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    result = negator.negate()
    print(result)
    print(negator.value)