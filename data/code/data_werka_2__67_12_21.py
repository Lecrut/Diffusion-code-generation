def find_zero_sum_pairs(nums):
    num_dict = {}
    pairs = set()
    
    for num in nums:
        if -num in num_dict:
            pairs.add((min(num, -num), max(num, -num)))
        num_dict[num] = True
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [5, -5, 10, -10, 3, -3, 7, 8]
    result = find_zero_sum_pairs(sample_values)
    print(result)