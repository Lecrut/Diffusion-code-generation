def max_subarray_sum(nums):
    current_max = global_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    return global_max

if __name__ == '__main__':
    sample_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(sample_values))