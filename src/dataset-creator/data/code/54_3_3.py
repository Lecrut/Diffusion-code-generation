import math
from typing import List, Tuple
def find_midpoint(arr: List[float]) -> float:
    if not arr:
        raise ValueError("Input array cannot be empty.")
    n = len(arr)
    mid_index = (n - 1) // 2
    return arr[mid_index]
if __name__ == '__main__':
    sample_data: List[float] = [4.0, 8.0, 3.5, 9.0, 7.0]
    try:
        midpoint_value = find_midpoint(sample_data)
        print(f"Input array length: {len(sample_data)}")
        print(f"Midpoint value at index {(len(sample_data)-1)//2}: {midpoint_value}")
    except ValueError as e:
        print(f"Error encountered: {e}")