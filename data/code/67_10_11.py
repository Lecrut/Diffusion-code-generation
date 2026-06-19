def find_pair_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == '__main__':
    SAMPLE_NUMBERS = [3, 5, -4, 8, 11, 1, -1, 6]
    TARGET_SUM = 10
    result = find_pair_sum(SAMPLE_NUMBERS, TARGET_SUM)
    print(result)