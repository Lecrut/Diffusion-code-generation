class ZeroSumFinder:
    def __init__(self, nums):
        self.nums = nums

    @staticmethod
    def _is_zero_sum_pair(num1, num2):
        return num1 + num2 == 0

    def find_pairs(self):
        seen = set()
        pairs = set()
        for num in self.nums:
            if -num in seen and ZeroSumFinder._is_zero_sum_pair(num, -num):
                pairs.add((min(num, -num), max(num, -num)))
            seen.add(num)
        return list(pairs)

if __name__ == '__main__':
    sample_values = [3, -3, 1, -1, 2, -2, 4, -4, 0]
    finder = ZeroSumFinder(sample_values)
    result = finder.find_pairs()
    print(result)