class Kadane:

    def __init__(self, nums):
        self.nums = nums

    def max_subarray_sum(self):
        max_current = max_global = self.nums[0]
        for num in self.nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
if __name__ == '__main__':
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    kadane_instance = Kadane(sample_array)
    result = kadane_instance.max_subarray_sum()
    print(result)