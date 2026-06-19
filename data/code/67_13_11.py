def find_zero_sum_pairs(nums):
    num_set = set(nums)
    pairs = set()
    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in pairs:
            pairs.add((min(num, -num), max(num, -num)))
    return list(pairs)

if __name__ == '__main__':
    sample_values = [5, -5, 10, -10, 3, 7, -7, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)