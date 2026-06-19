def find_zero_sum_pairs(nums):
    num_map = {}
    pairs = set()
    
    for num in nums:
        if -num in num_map:
            pairs.add((min(num, -num), max(num, -num)))
        num_map[num] = True
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, 4, -4, 5, -5]
    result = find_zero_sum_pairs(sample_values)
    print(result)