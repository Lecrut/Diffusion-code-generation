class BooleanFlagger:
    FLAG_ON = True
    FLAG_OFF = False
    def __init__(self, initial: bool) -> None:
        self.flag = initial
    def invert(self) -> bool:
        self.flag = not self.flag
        return self.flag
if __name__ == '__main__':
    flagger = BooleanFlagger(True)
    print(flagger.invert())
    print(flagger.invert())
    print(flagger.invert())