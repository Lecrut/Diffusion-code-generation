class MinMaxFinder:
    def __init__(self):
        self.current_min = None
        self.current_max = None

    def update(self, value):
        if self.current_min is None or value < self.current_min:
            self.current_min = value
        if self.current_max is None or value > self.current_max:
            self.current_max = value

    def get_min(self):
        return self.current_min

    def get_max(self):
        return self.current_max

if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    finder = MinMaxFinder()
    for value in data1:
        finder.update(value)
    print(f"Data 1: Min: {finder.get_min()}, Max: {finder.get_max()}")