class BooleanFlipper:
    def __init__(self, initial: bool = False) -> None:
        self._state = initial

    def flip(self) -> bool:
        self._state = not self._state
        return self._state

def flip_bool_value(value: bool) -> bool:
    flipper = BooleanFlipper(value)
    return flipper.flip()

if __name__ == '__main__':
    print(flip_bool_value(True))
    print(flip_bool_value(False))
    flipper = BooleanFlipper(False)
    print(flipper.flip())
    print(flipper.flip())