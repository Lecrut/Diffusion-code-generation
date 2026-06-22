class TruthValueInverter:
    def __init__(self, initial_value: bool) -> None:
        self._value = initial_value

    def invert(self) -> bool:
        return self._value ^ 1

    def get_inverted(self) -> bool:
        return self._value ^ 1

def find_opposite_truth_value(value: bool) -> bool:
    inverter = TruthValueInverter(value)
    return inverter.invert()

if __name__ == '__main__':
    result_true = find_opposite_truth_value(True)
    result_false = find_opposite_truth_value(False)
    print(result_true)
    print(result_false)