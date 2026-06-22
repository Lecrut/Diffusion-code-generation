def filter_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    sample_values = [-10, 23, -5, 0, 7, -8, 15]
    negative_numbers = filter_negative_numbers(sample_values)
    print(negative_numbers)