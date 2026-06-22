class MinMaxFinder:
    def __init__(self, values):
        if not values:
            raise ValueError("Input list cannot be empty")
        self.values = values
        self.min_val = self.max_val = values[0]

    def find_min_max(self):
        for value in self.values[1:]:
            if value < self.min_val:
                self.min_val = value
            elif value > self.max_val:
                self.max_val = value
        return self.min_val, self.max_val

if __name__ == '__main__':
    finder = MinMaxFinder([3, 5, 1, 2, 4, 8, 6, 7])
    print(finder.find_min_max())