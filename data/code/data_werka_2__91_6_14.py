class BooleanInverter:
    def __init__(self, state: bool) -> None:
        self._state: bool = state

    def invert(self) -> bool:
        self._state = not self._state
        return self._state

    def get_state(self) -> bool:
        return self._state

    def apply(self, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError(f"Expected bool, got {type(value).__name__}")
        return not value

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.invert())
    print(inv.get_state())
    print(inv.invert())
    print(inv.apply(False))
    print(inv.get_state())