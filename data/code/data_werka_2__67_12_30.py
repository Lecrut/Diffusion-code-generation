def find_zero_sum_pairs(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")
    
    num_set = set(nums)
    unique_pairs = []

    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in unique_pairs:
            unique_pairs.append((min(num, -num), max(num, -num)))
    
    return unique_pairs

if __name__ == '__main__':
    sample_values = [-6, 6, 7, -7, 8, 9, -9, 0, 1]
    result = find_zero_sum_pairs(sample_values)
    print(result)