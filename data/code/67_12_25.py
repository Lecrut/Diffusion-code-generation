def find_zero_sum_pairs(nums):
    num_map = {}
    pairs = set()
    for num in nums:
        if -num in num_map:
            pairs.add((min(num, -num), max(num, -num)))
        num_map[num] = True
    return list(pairs)

if __name__ == '__main__':
    sample_values = [7, -7, 8, -8, 9, -9, 10, 0]
    result = find_zero_sum_pairs(sample_values)
    print(result)