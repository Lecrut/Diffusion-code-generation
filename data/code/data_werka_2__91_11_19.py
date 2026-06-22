class BooleanNegator:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> bool:
        return not self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.negate())