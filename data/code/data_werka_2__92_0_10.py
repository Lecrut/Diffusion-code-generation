class BooleanInverter:
    def __init__(self, initial_state: bool):
        self._state = initial_state

    def invert(self) -> bool:
        self._state = not self._state
        return self._state

    def get_current(self) -> bool:
        return self._state

if __name__ == '__main__':
    inverter = BooleanInverter(True)
    print(inverter.invert())
    print(inverter.get_current())

    inverter2 = BooleanInverter(False)
    print(inverter2.invert())
    print(inverter2.get_current())