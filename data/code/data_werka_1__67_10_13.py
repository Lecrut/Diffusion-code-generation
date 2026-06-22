def find_pair_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == '__main__':
    sample_nums = [3, 3, 6, 15]
    target_sum = 9
    result_indices = find_pair_sum(sample_nums, target_sum)
    print(result_indices)