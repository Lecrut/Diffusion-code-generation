def filter_negative_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num < 0]
if __name__ == '__main__':
    sample_data = [-5, -10, 3, 7, -2, 42, -9]
    result = filter_negative_numbers(sample_data)
    print(result)