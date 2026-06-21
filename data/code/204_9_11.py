def median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    return (nums[mid] + nums[~mid]) / 2

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(median(sample_values))