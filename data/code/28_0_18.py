class NumberPair:
    def __init__(self, first, second):
        self._values = (first, second)

    def get_sorted(self):
        return tuple(sorted(self._values))

if __name__ == '__main__':
    pair = NumberPair(10, 42)
    print(pair.get_sorted())
    print(pair.get_sorted())