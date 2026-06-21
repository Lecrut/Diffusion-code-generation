def find_zero_sum_pairs(nums):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers.")
    
    num_set = set(nums)
    pairs = set()
    
    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in pairs:
            pairs.add((min(num, -num), max(num, -num)))
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [10, -10, 5, -5, 3, 3, -3, 0, 2, -2]
    result = find_zero_sum_pairs(sample_values)
    print(result)