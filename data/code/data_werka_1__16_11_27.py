def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_numbers = [-10, -5, 0, 3, 7, -2, 8]
    positive_numbers = filter_positive_numbers(sample_numbers)
    print(positive_numbers)