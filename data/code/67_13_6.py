def find_zero_sum_pairs(nums):
    seen = set()
    pairs = set()
    for num in nums:
        if -num in seen:
            pairs.add((min(num, -num), max(num, -num)))
        seen.add(num)
    return list(pairs)

if __name__ == '__main__':
    SAMPLE_VALUES = [3, -3, 1, 2, -2, 0, 4, -4]
    result = find_zero_sum_pairs(SAMPLE_VALUES)
    print(result)