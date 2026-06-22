class MinMaxFinder:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def update(self, value):
        if self.min_val is None or value < self.min_val:
            self.min_val = value
        if self.max_val is None or value > self.max_val:
            self.max_val = value

    def get_min_max(self):
        return (self.min_val, self.max_val)

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_values = [10, 5, 20, 8, 15]
    for value in sample_values:
        finder.update(value)
    print(finder.get_min_max())