from typing import List, Union
def find_midpoint(arr: List[Union[int, float]]) -> int:
    if not arr:
        raise ValueError("Input array cannot be empty.")
    length = len(arr)
    midpoint_index = (length - 1) // 2
    return midpoint_index
if __name__ == '__main__':
    sample_array = [5, 10, 15, 20]
    result = find_midpoint(sample_array)
    print(f"Midpoint index: {result}")