class MinFinder:
    def __init__(self, data):
        self.data = iter(data)
        self.current_min = None

    def find_smallest(self):
        if not hasattr(self, 'current_min'):
            try:
                self.current_min = next(self.data)
            except StopIteration:
                return None
        for number in self.data:
            if number < self.current_min:
                self.current_min = number
        return self.current_min

if __name__ == '__main__':
    finder = MinFinder([10, 5, 2, 8, 1])
    print(finder.find_smallest())