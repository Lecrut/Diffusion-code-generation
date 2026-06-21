def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

if __name__ == '__main__':
    sample_values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = filter_odd_numbers(sample_values)
    print(result)