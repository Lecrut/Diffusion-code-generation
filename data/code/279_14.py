class RangeCycler:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start cannot be greater than end")
        self._range = list(range(start, end + 1))
        self._index = 0
    def get_next(self):
        if not self._range:
            return None
        result = self._range[self._index]
        self._index = (self._index + 1) % len(self._range)
        return result
if __name__ == '__main__':
    cycler = RangeCycler(1, 5)
    print("Cycling through range (1 to 5):")
    for _ in range(7):
        print(cycler.get_next(), end=" ")
    print("\n")
    cycler2 = RangeCycler(10, 13)
    print("Cycling through range (10 to 13):")
    for _ in range(5):
        print(cycler2.get_next(), end=" ")
    print("\n")
    cycler3 = RangeCycler(5, 5)
    print("Cycling through range (5 to 5):")
    for _ in range(4):
        print(cycler3.get_next(), end=" ")
    print("\n")