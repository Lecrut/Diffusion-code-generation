def find_smallest_missing_positive(nums):
    n = len(nums)
    if 1 not in nums:
        return 1
    contains_one = 1 in nums
    if not contains_one:
        return 1
    nums = [0] + nums
    n += 1
    for i in range(n):
        if nums[i] <= 0 or nums[i] >= n:
            nums[i] = n
    for i in range(1, n):
        index = abs(nums[i])
        if index == n:
            nums[0] = -abs(nums[0])
        else:
            nums[index] = -abs(nums[index])
    for i in range(1, n):
        if nums[i] > 0:
            return i
    return n
if __name__ == '__main__':
    sample_list = [3, 4, -1, 1]
    result = find_smallest_missing_positive(sample_list)
    print(result)
    sample_list2 = [7, 8, 9, 11, 12]
    result2 = find_smallest_missing_positive(sample_list2)
    print(result2)