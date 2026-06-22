class SecondSmallestFinder:
    def __init__(self):
        self.first = None
        self.second = None

    def add(self, value):
        if self.first is None or value < self.first:
            self.second = self.first
            self.first = value
        elif (self.second is None or value < self.second) and value != self.first:
            self.second = value

    def get_second_smallest(self):
        return self.second

if __name__ == '__main__':
    finder = SecondSmallestFinder()
    for value in [45, 12, 89, 3, 56, 78]:
        finder.add(value)
    print(finder.get_second_smallest())