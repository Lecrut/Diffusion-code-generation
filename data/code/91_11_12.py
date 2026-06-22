class BooleanInverter:
    INVERTED_TRUE = False
    INVERTED_FALSE = True
    FALSE_STATE = False
    TRUE_STATE = True

    def __init__(self, state: bool) -> None:
        self._current_state = state

    def is_true(self) -> bool:
        return self._current_state

    def invert(self) -> bool:
        if self._current_state is self.TRUE_STATE:
            self._current_state = self.INVERTED_TRUE
        else:
            self._current_state = self.INVERTED_FALSE
        return self._current_state

if __name__ == '__main__':
    inv = BooleanInverter(True)
    new_state = inv.invert()
    print(new_state)
    inv2 = BooleanInverter(False)
    print(inv2.invert())