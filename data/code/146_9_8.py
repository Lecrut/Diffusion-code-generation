class MaxSubarrayFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_max_subarray_sum(self):
        max_current = max_global = self.nums[0]
        for num in self.nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global

if __name__ == '__main__':
    sample_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    finder = MaxSubarrayFinder(sample_values)
    print(finder.find_max_subarray_sum())