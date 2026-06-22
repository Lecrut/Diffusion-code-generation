def find_zero_sum_pairs(nums):
    num_set = set(nums)
    zero_sum_pairs = set()
    
    for num in num_set:
        if -num in num_set and (min(num, -num), max(num, -num)) not in zero_sum_pairs:
            zero_sum_pairs.add((min(num, -num), max(num, -num)))
    
    return list(zero_sum_pairs)

if __name__ == '__main__':
    sample_values = [-3, 0, 2, 3, -1, 1, 4, -4, 5]
    result = find_zero_sum_pairs(sample_values)
    print(result)