class PairSumFinder:

    def __init__(self, nums):
        self.nums = nums

    def find_pair_sum(self, target):
        num_to_index = {}
        for index, num in enumerate(self.nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []
if __name__ == '__main__':
    nums = [3, 6, 8, 12, 15]
    target = 20
    finder = PairSumFinder(nums)
    result = finder.find_pair_sum(target)
    print(result)
    target2 = 14
    result2 = finder.find_pair_sum(target2)
    print(result2)