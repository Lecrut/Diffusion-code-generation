class MinMaxFinder:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def update_min_max(self, value):
        if self.min_val is None or value < self.min_val:
            self.min_val = value
        if self.max_val is None or value > self.max_val:
            self.max_val = value

    def get_results(self):
        return self.min_val, self.max_val

if __name__ == '__main__':
    finder = MinMaxFinder()
    data = [3.14, 1.618, 2.718, 0.577, 99.99, -100.5, 42]
    for value in data:
        finder.update_min_max(value)
    
    min_value, max_value = finder.get_results()
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")