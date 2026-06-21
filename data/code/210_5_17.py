from typing import List

def calculate_range(values: List[int]) -> int:
    if not values:
        raise ValueError("Input list cannot be empty")
    min_val = max_val = values[0]
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"Range of {sample_values}: {calculate_range(sample_values)}")