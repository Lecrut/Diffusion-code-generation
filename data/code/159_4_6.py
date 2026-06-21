def filter_odd_numbers(numbers):
    odd_nums = []
    for num in numbers:
        if num & 1:
            odd_nums.append(num)
    return odd_nums

if __name__ == '__main__':
    sample_values = [21, 43, 65, 87, 90, 111, 123]
    result = filter_odd_numbers(sample_values)
    print(result)