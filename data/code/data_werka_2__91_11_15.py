class BooleanSwitch:
    NEGATION_TABLE = {True: False, False: True}

    def __init__(self, initial: bool) -> None:
        self._active = initial

    @staticmethod
    def _negate(val: bool) -> bool:
        return BooleanSwitch.NEGATION_TABLE[val]

    def flip(self) -> bool:
        self._active = self._negate(self._active)
        return self._active

    def is_active(self) -> bool:
        return self._active

if __name__ == '__main__':
    switch = BooleanSwitch(True)
    first_flip = switch.flip()
    second_flip = switch.flip()
    print(first_flip)
    print(second_flip)
    print(switch.is_active())