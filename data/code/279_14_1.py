class RangeCycler:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start cannot be greater than end")
        self._range = list(range(start, end + 1))
        self._index = 0
    def cycle(self):
        if not self._range:
            return None
        value = self._range[self._index]
        self._index = (self._index + 1) % len(self._range)
        return value
if __name__ == '__main__':
    cycler = RangeCycler(1, 5)
    print("Cycling through range [1, 5]:")
    for _ in range(7):
        print(cycler.cycle())
    print("\nCycling through a different range [10, 12]:")
    cycler2 = RangeCycler(10, 12)
    for _ in range(5):
        print(cycler2.cycle())