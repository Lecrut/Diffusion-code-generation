def find_pair_sum(nums, target):
    num_map = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in num_map:
            return [num_map[complement], index]
        num_map[number] = index
    return []

if __name__ == '__main__':
    sample_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    result_indices = find_pair_sum(sample_numbers, target_sum)
    print(result_indices)