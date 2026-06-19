def find_zero_sum_pairs(nums):
    num_set = set(nums)
    pairs = set()
    for num in nums:
        if -num in num_set and (min(num, -num), max(num, -num)) not in pairs:
            pairs.add((min(num, -num), max(num, -num)))
    return list(pairs)

if __name__ == '__main__':
    sample_values = [3, -3, 2, -2, 1, -1, 0, 4, -4]
    result = find_zero_sum_pairs(sample_values)
    print(result)