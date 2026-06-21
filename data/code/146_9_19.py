def validate_input(arr):
    if not arr:
        raise ValueError("Input array cannot be empty")
    for num in arr:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements of the array must be numbers")

def max_subarray_sum(nums):
    validate_input(nums)
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

if __name__ == '__main__':
    sample_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(sample_values))