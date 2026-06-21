def filter_odd_numbers(nums):
    odd_nums = []
    for num in nums:
        if num & 1:
            odd_nums.append(num)
    return odd_nums

if __name__ == '__main__':
    test_values = [23, 45, 67, 89, 10, 11, 13]
    result = filter_odd_numbers(test_values)
    print(result)