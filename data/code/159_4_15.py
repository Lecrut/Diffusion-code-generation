def filter_odd_numbers(nums):
    return [num for num in nums if num & 1]

if __name__ == '__main__':
    test_values = [23, 45, 67, 89, 10, 11, 13]
    print(filter_odd_numbers(test_values))