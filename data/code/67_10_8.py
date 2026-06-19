def find_pair_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []

if __name__ == '__main__':
    sample_nums = [3, 6, 8, 12]
    sample_target = 14
    result_indices = find_pair_sum(sample_nums, sample_target)
    print(result_indices)