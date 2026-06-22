def find_median(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        mid_right_index = n // 2
        mid_left_index = mid_right_index - 1
        return (nums[mid_left_index] + nums[mid_right_index]) / 2.0

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(f"Median of {sample_list}: {find_median(sample_list)}")