class BooleanNegator:
    def __init__(self, initial_value: bool = False):
        self._value = initial_value

    def get_value(self) -> bool:
        return self._value

    def set_value(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"Expected bool, got {type(value).__name__}")
        self._value = value

    def negate(self) -> bool:
        self._value = not self._value
        return self._value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    print(negator.negate())
    negator.set_value(False)
    print(negator.negate())
    print(negator.get_value())