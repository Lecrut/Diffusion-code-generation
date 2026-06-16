from typing import List
def filter_positive_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    data = [-5, -2.3, 10, 4, -7, 89, 0]
    cleaned_data = filter_positive_numbers(data)
    print(cleaned_data)