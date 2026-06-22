class ZeroSumPairFinder:
    def __init__(self, nums):
        self.nums = nums
        self.seen = set()
        self.pairs = set()

    def find_pairs(self):
        for num in self.nums:
            if -num in self.seen:
                self.pairs.add((min(num, -num), max(num, -num)))
            self.seen.add(num)
        return list(self.pairs)

if __name__ == '__main__':
    sample_values = [1, 2, -1, -2, 3, -3, 0, 4, -4]
    finder = ZeroSumPairFinder(sample_values)
    result = finder.find_pairs()
    print(result)