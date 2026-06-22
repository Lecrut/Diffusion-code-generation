class ZeroSumPairFinder:
    def __init__(self, nums):
        self.nums = nums

    @staticmethod
    def _is_valid_input(nums):
        return isinstance(nums, list) and all(isinstance(x, int) for x in nums)

    def find_pairs(self):
        if not ZeroSumPairFinder._is_valid_input(self.nums):
            raise ValueError("Input must be a list of integers.")
        
        seen = set()
        pairs = set()
        for num in self.nums:
            if -num in seen:
                pairs.add((min(num, -num), max(num, -num)))
            seen.add(num)
        return list(pairs)

if __name__ == '__main__':
    sample_values = [6, -6, 7, -7, 8, -8, 9, 0]
    finder = ZeroSumPairFinder(sample_values)
    result = finder.find_pairs()
    print(result)