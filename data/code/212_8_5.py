def find_second_extremes(nums):
    if len(nums) < 2:
        return (None, None)
    min_val = max_val = nums[0]
    second_min = second_max = float('inf')
    for num in nums:
        if num < min_val:
            second_min = min_val
            min_val = num
        elif min_val < num < second_min:
            second_min = num
        if num > max_val:
            second_max = max_val
            max_val = num
        elif max_val > num > second_max:
            second_max = num
    return (second_min if second_min != float('inf') else None, second_max if second_max != float('inf') else None)
if __name__ == '__main__':
    sample_nums = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_second_extremes(sample_nums))