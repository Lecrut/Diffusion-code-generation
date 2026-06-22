class BooleanState:
    _NEGATION_TABLE = {True: False, False: True}

    def __init__(self, initial_value: bool) -> None:
        self._current_value = initial_value

    def get_value(self) -> bool:
        return self._current_value

    def set_value(self, new_value: bool) -> None:
        self._current_value = new_value

    def negate(self) -> bool:
        self._current_value = self._NEGATION_TABLE[self._current_value]
        return self._current_value

if __name__ == '__main__':
    state = BooleanState(True)
    print(state.negate())
    print(state.get_value())
    state.set_value(False)
    print(state.negate())
    print(state.get_value())