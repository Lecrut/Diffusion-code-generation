class LogicalInverter:
    def __init__(self, flag: bool) -> None:
        self._current_state = flag
    def invert(self) -> bool:
        previous = self._current_state
        self._current_state = not previous
        return self._current_state
    def get_state(self) -> bool:
        return self._current_state
if __name__ == '__main__':
    inverter = LogicalInverter(False)
    new_state = inverter.invert()
    print(new_state)
    current = inverter.get_state()
    print(current)