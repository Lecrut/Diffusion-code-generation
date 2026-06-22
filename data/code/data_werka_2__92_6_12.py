class BooleanInverter:
    OPPOSITE_MAP = {True: False, False: True}
    DEFAULT_STATE = False

    def __init__(self, state: bool = DEFAULT_STATE):
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean")
        self._current_state = state

    def get_opposite(self) -> bool:
        return self.OPPOSITE_MAP[self._current_state]

    def toggle(self) -> bool:
        self._current_state = not self._current_state
        return self._current_state

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.get_opposite())
    print(inv.toggle())
    print(inv.get_opposite())
    try:
        BooleanInverter(1)
    except ValueError as e:
        print(e)