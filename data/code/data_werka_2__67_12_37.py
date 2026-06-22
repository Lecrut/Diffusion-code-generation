def find_zero_sum_pairs(nums):
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements must be integers.")
    
    num_set = set(nums)
    pairs = set()
    
    for num in nums:
        complement = -num
        if complement in num_set and (min(num, complement), max(num, complement)) not in pairs:
            pairs.add((min(num, complement), max(num, complement)))
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [7, -7, 3, -3, 2, -2, 0, 5, -5]
    result = find_zero_sum_pairs(sample_values)
    print(result)