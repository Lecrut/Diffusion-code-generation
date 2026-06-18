def filter_positive_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num > 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 0, 3, 7, 89, 42]
    result_set: list[int] = filter_positive_numbers(sample_data)
    print(result_set)