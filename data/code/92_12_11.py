class BooleanInverter:
    MASK: int = 1

    def __init__(self, initial_value: bool) -> None:
        self._current_value: bool = initial_value

    def invert(self) -> bool:
        self._current_value = bool(self._current_value ^ self.MASK)
        return self._current_value

    def get_value(self) -> bool:
        return self._current_value

def find_opposite_truth_value(value: bool) -> bool:
    inverter = BooleanInverter(value)
    return inverter.invert()

if __name__ == '__main__':
    result_true = find_opposite_truth_value(True)
    result_false = find_opposite_truth_value(False)
    print(result_true)
    print(result_false)
    inverter = BooleanInverter(True)
    print(inverter.invert())
    print(inverter.get_value())