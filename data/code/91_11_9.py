class BooleanSwitch:
    def __init__(self, initial_state: bool) -> None:
        self._active = initial_state

    def flip_state(self) -> bool:
        current_status = self._active
        new_status = not current_status
        self._active = new_status
        return new_status

    def get_state(self) -> bool:
        return self._active

if __name__ == '__main__':
    switch = BooleanSwitch(False)
    new_status = switch.flip_state()
    print(new_status)
    print(switch.get_state())