def find_pair_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == '__main__':
    sample_nums = [10, 15, 3, 7]
    sample_target = 17
    result = find_pair_sum(sample_nums, sample_target)
    print(result)