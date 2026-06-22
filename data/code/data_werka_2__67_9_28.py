class TwoSumFinder:
    def __init__(self):
        self.num_to_index = {}

    @staticmethod
    def validate_input(nums, target):
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a list of integers")
        if not isinstance(target, int):
            raise ValueError("target must be an integer")

    def find_pair_sum(self, nums, target):
        self.validate_input(nums, target)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in self.num_to_index:
                return [self.num_to_index[complement], index]
            self.num_to_index[num] = index
        raise ValueError("No two sum solution")

if __name__ == '__main__':
    finder = TwoSumFinder()
    nums = [4, 9, 11, 3]
    target = 15
    result = finder.find_pair_sum(nums, target)
    print(result)