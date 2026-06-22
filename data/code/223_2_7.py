class MaxFinder:
    def __init__(self):
        self.max_value = None

    def update_max(self, value):
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def get_max(self):
        return self.max_value

if __name__ == '__main__':
    finder = MaxFinder()
    for value in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]:
        finder.update_max(value)
    print(f"Maximum: {finder.get_max()}")