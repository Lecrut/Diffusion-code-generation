class BooleanFlipper:
    FLIP_MAP = {True: False, False: True}

    def __init__(self, flag: bool):
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        self._flag = flag

    def get_opposite(self) -> bool:
        return self.FLIP_MAP[self._flag]

    def flip(self) -> bool:
        self._flag = not self._flag
        return self._flag

if __name__ == '__main__':
    flipper = BooleanFlipper(True)
    print(flipper.get_opposite())
    print(flipper.flip())
    print(flipper.get_opposite())
    flipper._flag = False
    print(flipper.get_opposite())
    try:
        BooleanFlipper(1)
    except ValueError as e:
        print(e)