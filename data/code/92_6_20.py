class BooleanInverter:
    _OPPOSITES = {True: False, False: True}

    def __init__(self, state: bool):
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean")
        self._state = state

    def get_opposite(self) -> bool:
        return self._OPPOSITES[self._state]

    def toggle(self) -> bool:
        self._state = not self._state
        return self._state

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.get_opposite())
    print(inv.toggle())
    print(inv.get_opposite())
    try:
        BooleanInverter(1)
    except ValueError:
        print("ValueError raised for non-boolean input")