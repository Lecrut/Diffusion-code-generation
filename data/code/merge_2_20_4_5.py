from typing import List
def filter_non_negative_numbers(numbers: List[float]) -> List[int]:
    return [num for num in numbers if isinstance(num, int) and num >= 0]
if __name__ == '__main__':
    sample_data = [-5, -2, 0, 3, 7, 10.9, 42]
    result_set: List[int] = filter_non_negative_numbers(sample_data)
    print(f"Input: {sample_data}")
    print(f"Filtered Result Set: {result_set}")