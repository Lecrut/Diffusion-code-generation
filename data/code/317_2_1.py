class RangeCycler:
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
    def print_range(self):
        for i in range(self.min, self.max + 1):
            print(i)
if __name__ == '__main__':
    cycler = RangeCycler(5, 12)
    cycler.print_range()