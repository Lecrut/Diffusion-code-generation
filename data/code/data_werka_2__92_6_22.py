class BooleanInverter:
    def __init__(self, state: bool):
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean")
        self._state = state

    def get_opposite(self) -> bool:
        if self._state:
            return False
        return True

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.get_opposite())
    inv._state = False
    print(inv.get_opposite())