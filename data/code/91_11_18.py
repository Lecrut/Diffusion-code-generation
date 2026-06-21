class BooleanProcessor:
    def __init__(self, initial: bool) -> None:
        self._value = initial

    def get_value(self) -> bool:
        return self._value

    def set_value(self, new_value: bool) -> None:
        self._value = new_value

    def toggle(self) -> bool:
        self._value = not self._value
        return self._value

    def negate(self) -> bool:
        return not self._value

    def is_positive(self) -> bool:
        return bool(self._value)

if __name__ == '__main__':
    processor = BooleanProcessor(True)
    print(processor.toggle())
    print(processor.get_value())
    print(processor.negate())
    processor.set_value(False)
    print(processor.is_positive())
    print(processor.toggle())
    print(processor.get_value())