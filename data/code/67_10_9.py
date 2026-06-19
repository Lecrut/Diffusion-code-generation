def find_pair_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

if __name__ == '__main__':
    sample_nums = [3, 6, 8, 12, 15]
    target_value = 14
    result_indices = find_pair_sum(sample_nums, target_value)
    print(result_indices)