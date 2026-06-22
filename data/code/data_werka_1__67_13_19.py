def find_zero_sum_pairs(nums):
    num_set = set(nums)
    unique_pairs = set()
    
    for num in num_set:
        if -num in num_set:
            pair = (min(num, -num), max(num, -num))
            unique_pairs.add(pair)
    
    return list(unique_pairs)

if __name__ == '__main__':
    sample_values = [7, -7, 5, -5, 3, 0, 9, -9]
    result = find_zero_sum_pairs(sample_values)
    print(result)