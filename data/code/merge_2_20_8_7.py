from typing import List
def remove_negative_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    sample_data = [-5, -1, 0, 3, -2, 7, -8]
    cleaned_data = remove_negative_numbers(sample_data)
    print(cleaned_data)