def filter_positive_numbers(numbers: list) -> list:
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 7, 0, 2.8]
    result = filter_positive_numbers(sample_data)
    print(result)