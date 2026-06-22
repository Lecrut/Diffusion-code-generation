def find_zero_sum_pairs(nums):
    num_set = set(nums)
    pairs = set()
    
    for num in nums:
        if -num in num_set and (num, -num) not in pairs and (num, -num) != (-num, num):
            pairs.add((min(num, -num), max(num, -num)))
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [1, -1, 2, -2, 3, 4, -4, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)