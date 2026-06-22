def find_zero_sum_pairs(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")
    num_set = set(nums)
    unique_pairs = set()
    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in unique_pairs:
            unique_pairs.add((min(num, -num), max(num, -num)))
    return list(unique_pairs)

if __name__ == '__main__':
    sample_values = [6, -6, 7, -7, 8, -8, 9, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)