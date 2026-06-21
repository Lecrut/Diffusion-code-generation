class BooleanState:
    def __init__(self, initial_value: bool):
        self._state = initial_value

    def get_opposite(self) -> bool:
        return not self._state

if __name__ == '__main__':
    state = BooleanState(True)
    print(state.get_opposite())
    state._state = False
    print(state.get_opposite())