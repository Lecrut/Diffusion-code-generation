def filter_positive_numbers(numbers):
    return [num for num in numbers if isinstance(num, (int, float)) and num >= 0]
if __name__ == '__main__':
    sample_data = [-5, "not a number", -3.2, None, 0, 4.7, "", True, False, -10]
    result = filter_positive_numbers(sample_data)
    print(result)