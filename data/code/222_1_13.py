class MinFinder:
    def __init__(self):
        self.min_value = None

    def update_min(self, value):
        if self.min_value is None or value < self.min_value:
            self.min_value = value

    def get_min(self):
        return self.min_value

if __name__ == '__main__':
    finder = MinFinder()
    sample_values = [10, 5, 20, 3, 15]
    for value in sample_values:
        finder.update_min(value)
    print(finder.get_min())