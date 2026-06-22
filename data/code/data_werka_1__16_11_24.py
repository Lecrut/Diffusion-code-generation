def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_values = [-10, -5, 0, 5, 10, 15]
    positive_numbers = filter_positive_numbers(sample_values)
    print(positive_numbers)