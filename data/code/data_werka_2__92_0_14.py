class BooleanInverter:
    def __init__(self, initial_value: bool):
        self._current_value = initial_value

    def invert(self) -> bool:
        self._current_value = not self._current_value
        return self._current_value

    def get_value(self) -> bool:
        return self._current_value

def get_opposite_truth_value(value: bool) -> bool:
    inverter = BooleanInverter(value)
    return inverter.invert()

if __name__ == '__main__':
    test_true = True
    test_false = False

    result_true = get_opposite_truth_value(test_true)
    print(result_true)

    obj = BooleanInverter(test_false)
    result_false = obj.invert()
    print(result_false)
    print(obj.get_value())