def find_median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2.0
    else:
        return nums[mid]

if __name__ == '__main__':
    sample_values = [7, 5, 3, 1, 4, 6, 8]
    median_value = find_median(sample_values)
    print(f"The median is: {median_value}")