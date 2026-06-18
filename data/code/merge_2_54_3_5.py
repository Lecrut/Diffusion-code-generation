from typing import List
def find_midpoint(arr: List[float]) -> float:
    if not arr:
        raise ValueError("Array cannot be empty.")
    total = sum(arr)
    return total / 2
if __name__ == '__main__':
    sample_array = [1.0, 3.0, 5.0]
    midpoint = find_midpoint(sample_array)
    print(f"Midpoint: {midpoint}")