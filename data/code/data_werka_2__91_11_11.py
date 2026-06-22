class BooleanFlagger:
    FLAG_TRUE = True
    FLAG_FALSE = False
    def __init__(self, state: bool) -> None:
        self._current = state
    def flip(self) -> bool:
        self._current = self.FLAG_FALSE if self._current else self.FLAG_TRUE
        return self._current
    def get(self) -> bool:
        return self._current
if __name__ == '__main__':
    flagger = BooleanFlagger(True)
    flipped = flagger.flip()
    print(flipped)
    print(flagger.get())