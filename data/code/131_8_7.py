class MaxSubarraySum:

    def find_max_subarray_sum(self, nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
if __name__ == '__main__':
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    calculator = MaxSubarraySum()
    result = calculator.find_max_subarray_sum(sample_array)
    print(result)