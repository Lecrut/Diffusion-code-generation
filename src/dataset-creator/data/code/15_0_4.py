from typing import List, Union
def safe_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    if not numbers:
        return []
    try:
        sorted_numbers = sorted(numbers)
        return sorted_numbers
    except TypeError as e:
        raise ValueError(f"List contains non-numeric elements. Error details: {e}")
if __name__ == '__main__':
    sample_data = [3, 1.5, '2', None, -4, True]
    try:
        result = safe_sort(sample_data)
        print("Sorted list:", result)
    except ValueError as ve:
        print(f"Error occurred during sorting: {ve}")