def find_zero_sum_pairs(nums):
    if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums):
        raise ValueError("Input must be a list of integers.")
    
    num_set = set(nums)
    pairs = []
    
    for num in num_set:
        if num < 0 and -num in num_set:
            pairs.append((num, -num))
    
    return pairs

if __name__ == '__main__':
    sample_values = [1, -1, 2, -2, 3, 4, -4, 5, -5, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)