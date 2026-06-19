def find_zero_sum_pairs(nums):
    num_set = set(nums)
    unique_pairs = set()
    
    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in unique_pairs:
            unique_pairs.add((min(num, -num), max(num, -num)))
    
    return list(unique_pairs)

if __name__ == '__main__':
    sample_values = [5, -5, 10, -10, 3, 7, -3, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)