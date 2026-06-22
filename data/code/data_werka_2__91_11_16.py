class BooleanInverter:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False

    def __init__(self, flag: bool) -> None:
        self._flag = flag

    def invert(self) -> bool:
        self._flag = not self._flag
        return self._flag

    def get_flag(self) -> bool:
        return self._flag

if __name__ == '__main__':
    inv = BooleanInverter(True)
    print(inv.invert())
    print(inv.get_flag())
    print(inv.invert())
    print(inv.get_flag())