def filter_positive_numbers(numbers):
    POSITIVE_THRESHOLD = 0
    return [num for num in numbers if num > POSITIVE_THRESHOLD]

if __name__ == '__main__':
    sample_values = [-5, -2, 0, 4, 6, -8, 10]
    positive_numbers = filter_positive_numbers(sample_values)
    print(positive_numbers)