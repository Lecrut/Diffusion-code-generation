def find_pair_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == '__main__':
    SAMPLE_NUMS = [3, 6, 8, 12, 15]
    TARGET_SUM = 19
    result = find_pair_sum(SAMPLE_NUMS, TARGET_SUM)
    print(result)