class RangeCycler:
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
    def print_range(self):
        for i in range(self.min, self.max + 1):
            print(i)
if __name__ == '__main__':
    r = RangeCycler(5, 10)
    r.print_range()