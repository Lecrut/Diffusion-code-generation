from typing import List

def validate_numeric_list(data: List[int]) -> None:
    if not all(isinstance(item, int) for item in data):
        raise ValueError("All elements in the list must be integers.")

def calculate_range(data: List[int]) -> int:
    min_val = min(data)
    max_val = max(data)
    return max_val - min_val

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    validate_numeric_list(sample_values)
    range_value = calculate_range(sample_values)
    print(f"The range of the list is: {range_value}")