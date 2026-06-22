def find_smallest_missing_positive(nums):
    n = len(nums)
    if 1 not in nums:
        return 1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1
    for i in range(n):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1

if __name__ == '__main__':
    sample_values = [3, 4, -1, 1]
    print(find_smallest_missing_positive(sample_values))