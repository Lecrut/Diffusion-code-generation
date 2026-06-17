import math
from typing import List, Union
def find_midpoint(arr: List[Union[int, float]]) -> int:
    if not arr:
        raise ValueError("Input array cannot be empty.")
    n = len(arr)
    return (n - 1) // 2
if __name__ == '__main__':
    sample_array = [50.0, 60.0, 70.0]
    midpoint_index = find_midpoint(sample_array)
    print(f"Midpoint index: {midpoint_index}")