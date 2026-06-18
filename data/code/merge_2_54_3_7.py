import math
from typing import List, Tuple
def find_midpoint(arr: List[float]) -> float:
    if not arr:
        raise ValueError("Input array cannot be empty.")
    n = len(arr)
    mid_index = (n - 1) // 2
    return arr[mid_index]
if __name__ == '__main__':
    sample_array: List[float] = [4.0, 8.0, 3.5, 9.0, 7.0]
    try:
        midpoint_value = find_midpoint(sample_array)
        print(f"Midpoint value at index {(len(sample_array)-1)//2}: {midpoint_value}")
        sample_even: List[float] = [1.0, 2.0, 3.0, 4.0]
        midpoint_even_index = (len(sample_even) - 1) // 2
        print(f"Even length array index {midpoint_even_index}: {sample_even[midpoint_even_index]}")
    except ValueError as e:
        print(f"Error encountered: {e}")