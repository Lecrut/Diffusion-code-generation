def filter_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    sample_values = [-10, 20, -30, 40, -50, 60]
    negative_numbers = filter_negative_numbers(sample_values)
    print(negative_numbers)