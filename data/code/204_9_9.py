def find_median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2.0
    else:
        return nums[mid]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_values))