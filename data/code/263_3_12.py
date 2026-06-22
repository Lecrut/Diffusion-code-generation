def find_smallest_missing_positive(nums):
    n = len(nums)
    contains_one = False
    for num in nums:
        if num == 1:
            contains_one = True
            break
    if not contains_one:
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
    sample_list = [3, 4, -1, 1]
    result = find_smallest_missing_positive(sample_list)
    print(result)