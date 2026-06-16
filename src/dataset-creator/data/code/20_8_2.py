import sys
def filter_positive_numbers(data: list[int]) -> list[int]:
    return [num for num in data if num >= 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 0, 3, 7, -2, 9, -4]
    cleaned_data: list[int] = filter_positive_numbers(sample_data)
    print(cleaned_data)