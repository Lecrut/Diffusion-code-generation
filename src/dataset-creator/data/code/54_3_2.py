from typing import List
def find_midpoint(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    total = sum(numbers)
    return total / 2
if __name__ == '__main__':
    sample_data = [10.5, 20.3, 30.7]
    midpoint_value = find_midpoint(sample_data)
    print(f"Midpoint of {sample_data} is: {midpoint_value}")