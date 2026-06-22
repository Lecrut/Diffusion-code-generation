class BooleanNegator:
    NEGATION_MAP = {True: False, False: True}

    def __init__(self, initial_value: bool) -> None:
        self._value = initial_value

    def get_value(self) -> bool:
        return self._value

    def set_value(self, value: bool) -> None:
        self._value = value

    def negate(self) -> bool:
        self._value = self.NEGATION_MAP.get(self._value, not self._value)
        return self._value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    result = negator.negate()
    print(result)
    print(negator.get_value())
    negator.set_value(False)
    print(negator.negate())