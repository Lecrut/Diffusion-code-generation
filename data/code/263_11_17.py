class MinMaxFinder:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def add(self, num):
        if self.min_val is None or num < self.min_val:
            self.min_val = num
        if self.max_val is None or num > self.max_val:
            self.max_val = num

    def get_min(self):
        return self.min_val

    def get_max(self):
        return self.max_val

if __name__ == '__main__':
    finder = MinMaxFinder()
    numbers = [10, 3, 7, 25, -5, 0]
    for number in numbers:
        finder.add(number)
    print(f"Smallest: {finder.get_min()}, Largest: {finder.get_max()}")