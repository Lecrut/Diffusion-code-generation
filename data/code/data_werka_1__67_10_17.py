class PairSumSolver:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair_sum(self):
        num_to_index = {}
        for index, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []

if __name__ == '__main__':
    nums = [10, 15, 3, 7]
    target = 17
    solver = PairSumSolver(nums, target)
    result = solver.find_pair_sum()
    print(result)