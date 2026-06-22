SMALL_POSITIVE = 1

def find_smallest_missing_positive(nums):
    n = len(nums)
    if n == 0:
        return SMALL_POSITIVE
    contains_one = any((num == SMALL_POSITIVE for num in nums))
    if not contains_one:
        return SMALL_POSITIVE
    nums[SMALL_POSITIVE - 1] = SMALL_POSITIVE
    for i in range(n):
        num = abs(nums[i])
        if num > n or num < SMALL_POSITIVE:
            continue
        index = num - 1
        nums[index] = -abs(nums[index])
    for i in range(1, n):
        if nums[i] > 0:
            return i + 1
    return n + 1
if __name__ == '__main__':
    sample_list = [3, 4, -1, 1]
    result = find_smallest_missing_positive(sample_list)
    print(result)
    another_sample_list = [7, 8, 9, 11, 12]
    result = find_smallest_missing_positive(another_sample_list)
    print(result)