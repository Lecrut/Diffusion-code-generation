class MinMaxFinder:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def update(self, value):
        if value < self.min_val:
            self.min_val = value
        elif value > self.max_val:
            self.max_val = value

    def get_min_max(self):
        return self.min_val, self.max_val

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_values = [3.141592653589793, 2.718281828459045, 1.4142135623730951, 0.5772156649015328]
    for value in sample_values:
        finder.update(value)
    min_val, max_val = finder.get_min_max()
    print(f"Minimum: {min_val}, Maximum: {max_val}")