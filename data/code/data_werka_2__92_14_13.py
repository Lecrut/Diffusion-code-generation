class BooleanInverter:
    def __init__(self, initial_value=False):
        self._current = initial_value

    def invert(self):
        self._current = not self._current
        return self._current

    def get_current(self):
        return self._current

if __name__ == '__main__':
    inverter = BooleanInverter(True)
    result1 = inverter.invert()
    print(result1)
    inverter2 = BooleanInverter(False)
    result2 = inverter2.invert()
    print(result2)