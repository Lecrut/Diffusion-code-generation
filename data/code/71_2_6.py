def find_middle_value(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_values))