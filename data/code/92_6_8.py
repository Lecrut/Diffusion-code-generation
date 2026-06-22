class LogicSwitch:
    _OPPOSITES = {
        True: False,
        False: True
    }

    def __init__(self, active: bool):
        if not isinstance(active, bool):
            raise ValueError("State must be boolean")
        self._active = active

    def get_opposite_state(self) -> bool:
        return self._OPPOSITES[self._active]

    def is_active(self) -> bool:
        return self._active

if __name__ == '__main__':
    switch_on = LogicSwitch(True)
    print(switch_on.get_opposite_state())
    print(switch_on.is_active())

    switch_off = LogicSwitch(False)
    print(switch_off.get_opposite_state())
    print(switch_off.is_active())