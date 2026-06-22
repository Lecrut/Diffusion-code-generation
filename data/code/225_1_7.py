class MinMaxFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data
        self.min_val = None
        self.max_val = None

    def find_min_max(self):
        for x in self.data:
            if self.min_val is None or x < self.min_val:
                self.min_val = x
            if self.max_val is None or x > self.max_val:
                self.max_val = x

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MinMaxFinder(sample_list)
    finder.find_min_max()
    print(f"Minimum: {finder.min_val}, Maximum: {finder.max_val}")