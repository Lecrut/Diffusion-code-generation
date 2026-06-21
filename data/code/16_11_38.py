def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_values = [-5, -1, 2, 6, -8, 0, 7]
    positive_numbers = filter_positive_numbers(sample_values)
    print(positive_numbers)