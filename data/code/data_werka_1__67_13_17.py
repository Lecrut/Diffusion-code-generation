class ZeroSumPairsFinder:
    def __init__(self, nums):
        self.nums = nums

    @staticmethod
    def find_pairs(nums):
        seen = set()
        pairs = set()
        for num in nums:
            if -num in seen:
                pairs.add((min(num, -num), max(num, -num)))
            seen.add(num)
        return list(pairs)

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, 4, -4, 5, -5]
    finder = ZeroSumPairsFinder(sample_values)
    result = ZeroSumPairsFinder.find_pairs(sample_values)
    print(result)