class SmallestFinder:
    def __init__(self, data):
        self.data = iter(data)
        self._smallest = None

    def find_smallest(self):
        if not hasattr(self, '_smallest'):
            try:
                self._smallest = next(self.data)
            except StopIteration:
                return None
        for number in self.data:
            if number < self._smallest:
                self._smallest = number
        return self._smallest

if __name__ == '__main__':
    finder = SmallestFinder([10, 5, 20, 3, 15])
    print(finder.find_smallest())