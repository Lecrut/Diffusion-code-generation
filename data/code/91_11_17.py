class BooleanSwitch:
    def __init__(self, initial_state: bool) -> None:
        self._current_state = initial_state

    def get_state(self) -> bool:
        return self._current_state

    def flip_state(self) -> bool:
        is_active = self._current_state
        self._current_state = not is_active
        return self._current_state

if __name__ == '__main__':
    switch = BooleanSwitch(False)
    new_state = switch.flip_state()
    print(new_state)
    print(switch.get_state())
    switch.flip_state()
    print(switch.get_state())