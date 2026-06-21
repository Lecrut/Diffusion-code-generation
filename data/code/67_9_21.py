class TwoSumSolver:
    def __init__(self):
        self.num_to_index = {}

    def find_pair_sum(self, nums, target):
        for index, num in enumerate(nums):
            complement = target - num
            if complement in self.num_to_index:
                return [self.num_to_index[complement], index]
            self.num_to_index[num] = index
        raise ValueError("No two sum solution")

if __name__ == '__main__':
    solver = TwoSumSolver()
    nums = [3, 2, 4, 6]
    target = 8
    result = solver.find_pair_sum(nums, target)
    print(result)