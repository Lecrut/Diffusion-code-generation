def group_by_remainder(nums):
    grouped = {}
    for num in nums:
        remainder = num % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(num)
    return grouped

if __name__ == '__main__':
    sample_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = group_by_remainder(sample_nums)
    print(result)