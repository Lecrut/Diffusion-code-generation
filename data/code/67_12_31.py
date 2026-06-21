def find_zero_sum_pairs(nums):
    num_set = set(nums)
    pairs = set()
    for num in nums:
        if num < 0 and -num in num_set:
            pairs.add((num, -num))
    return list(pairs)

if __name__ == '__main__':
    sample_values = [3, -3, 2, -2, 1, -1, 4, -4, 5]
    result = find_zero_sum_pairs(sample_values)
    print(result)