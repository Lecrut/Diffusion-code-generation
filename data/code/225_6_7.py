class MinMaxFinder:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def add_value(self, value):
        if value < self.min_val:
            self.min_val = value
        elif value > self.max_val:
            self.max_val = value

    def get_min_max(self):
        return self.min_val, self.max_val

if __name__ == '__main__':
    finder = MinMaxFinder()
    for value in [10, 5, 20, 3, 15]:
        finder.add_value(value)
    print(finder.get_min_max())