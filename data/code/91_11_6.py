class BooleanState:
    def __init__(self, initial: bool) -> None:
        self._state = initial

    def get_state(self) -> bool:
        return self._state

    def toggle(self) -> bool:
        if self._state:
            self._state = False
            return False
        self._state = True
        return True

if __name__ == '__main__':
    state = BooleanState(True)
    print(state.toggle())
    print(state.toggle())
    print(state.get_state())