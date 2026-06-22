def find_zero_sum_pairs(nums):
    SEEN_THRESHOLD = 0
    num_set = set(nums)
    result_pairs = set()
    for num in nums:
        if -num in num_set and num > SEEN_THRESHOLD:
            result_pairs.add((num, -num))
    return list(result_pairs)
if __name__ == '__main__':
    sample_values = [3, -3, 2, -2, 1, 4, -4, 0]
    pairs = find_zero_sum_pairs(sample_values)
    print(pairs)