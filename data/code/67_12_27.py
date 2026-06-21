def find_zero_sum_pairs(nums):
    seen = set()
    pairs = set()
    
    for num in nums:
        if -num in seen:
            pairs.add((min(num, -num), max(num, -num)))
        seen.add(num)
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [1, -1, 2, -2, 3, 0, 4, -4]
    result = find_zero_sum_pairs(sample_values)
    print(result)