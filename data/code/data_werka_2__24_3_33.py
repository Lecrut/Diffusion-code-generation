def filter_negative_numbers(numbers):
    return [num for num in numbers if num < 0]

if __name__ == '__main__':
    SAMPLE_VALUES = [10, -3, 7, -8, 2, -5]
    NEGATIVE_NUMBERS = filter_negative_numbers(SAMPLE_VALUES)
    print(NEGATIVE_NUMBERS)