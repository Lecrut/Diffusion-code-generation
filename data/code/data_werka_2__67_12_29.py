def find_zero_sum_pairs(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")
    
    num_set = set(nums)
    pairs = []
    seen_pairs = set()
    
    for num in nums:
        complement = -num
        if complement in num_set and (min(num, complement), max(num, complement)) not in seen_pairs:
            pairs.append((min(num, complement), max(num, complement)))
            seen_pairs.add((min(num, complement), max(num, complement)))
    
    return pairs

if __name__ == '__main__':
    sample_values = [6, -6, 7, -7, 8, -8, 9, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)