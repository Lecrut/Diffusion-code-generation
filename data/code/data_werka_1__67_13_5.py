class ZeroSumPairFinder:
    def __init__(self):
        self.seen = set()
        self.pairs = set()

    def add_number(self, num):
        if -num in self.seen:
            self.pairs.add((min(num, -num), max(num, -num)))
        self.seen.add(num)

    def get_pairs(self):
        return list(self.pairs)

if __name__ == '__main__':
    sample_values = [10, -10, 20, -20, 30, 40, -40, 0]
    finder = ZeroSumPairFinder()
    for value in sample_values:
        finder.add_number(value)
    result = finder.get_pairs()
    print(result)