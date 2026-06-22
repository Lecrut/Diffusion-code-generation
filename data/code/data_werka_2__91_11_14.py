class LogicSwitch:
    FLAG_TRUE = 1
    FLAG_FALSE = 0
    TRANSITIONS = {
        FLAG_TRUE: FLAG_FALSE,
        FLAG_FALSE: FLAG_TRUE
    }

    def __init__(self, state: bool) -> None:
        self._current_state: bool = state
        self._history: list[bool] = [state]

    def get_state(self) -> bool:
        return self._current_state

    def get_history(self) -> list[bool]:
        return list(self._history)

    def flip(self) -> bool:
        old_state = self._current_state
        new_state = not old_state
        self._current_state = new_state
        self._history.append(new_state)
        return new_state

    def invert_state(self) -> bool:
        return self.flip()

if __name__ == '__main__':
    switch = LogicSwitch(True)
    print(switch.flip())
    print(switch.get_state())
    print(switch.invert_state())
    print(switch.get_state())
    print(switch.get_history())