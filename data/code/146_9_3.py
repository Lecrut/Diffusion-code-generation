def max_subarray_sum(nums):
    current_max = global_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    return global_max

if __name__ == '__main__':
    sample_values = [5, -7, 3, 5, -2, 4, -1]
    print(max_subarray_sum(sample_values))