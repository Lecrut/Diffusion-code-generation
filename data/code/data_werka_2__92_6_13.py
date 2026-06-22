class StateInverter:
    def __init__(self, flag: bool):
        if not isinstance(flag, bool):
            raise ValueError("Flag must be a boolean")
        self._flag = flag

    def get_opposite(self) -> bool:
        current = self._flag
        result = not current
        return result

if __name__ == '__main__':
    inv = StateInverter(False)
    opposite = inv.get_opposite()
    print(opposite)
    inv._flag = True
    opposite = inv.get_opposite()
    print(opposite)