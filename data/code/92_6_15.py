class BitFlipper:
    OPPOSITES = {True: False, False: True}

    def __init__(self, state: bool):
        if not isinstance(state, bool):
            raise ValueError("State must be a boolean")
        self._state = state

    def get_opposite(self) -> bool:
        return self.OPPOSITES[self._state]

if __name__ == '__main__':
    flipper = BitFlipper(True)
    result = flipper.get_opposite()
    print(result)
    flipper._state = False
    result2 = flipper.get_opposite()
    print(result2)