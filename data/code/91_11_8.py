class TruthValue:
    TRUE = 1
    FALSE = 0
    MASK = 1

    def __init__(self, flag: bool) -> None:
        self._bit = int(flag) & self.MASK

    def is_true(self) -> bool:
        return self._bit == self.TRUE

    def negate(self) -> bool:
        self._bit = self._bit ^ self.MASK
        return self.is_true()

if __name__ == '__main__':
    state = TruthValue(False)
    print(state.negate())
    print(state.is_true())
    print(state.negate())
    print(state.is_true())