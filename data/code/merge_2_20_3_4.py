def filter_negative_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n < 0]
if __name__ == '__main__':
    sample_data = [-5, -10, 3, -7, 20, -4]
    result = filter_negative_numbers(sample_data)
    print(result)