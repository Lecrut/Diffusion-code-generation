class BooleanNegator:
    def __init__(self, value: bool) -> None:
        self.value = value

    def get_negated(self) -> bool:
        return not self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    result = negator.get_negated()
    print(result)