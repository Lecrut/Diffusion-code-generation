def extract_odd_numbers(nums):
    odd_nums = []
    for num in nums:
        if num & 1:
            odd_nums.append(num)
    return odd_nums

if __name__ == '__main__':
    test_values = [15, 22, 37, 41, 56, 63]
    result = extract_odd_numbers(test_values)
    print(result)