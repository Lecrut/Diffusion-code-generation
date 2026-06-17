import numpy as np
from typing import List, Union, Tuple
def find_center_mark(data: List[Union[int, float]]) -> int:
    if not data:
        raise ValueError("Input sequence cannot be empty.")
    n = len(data)
    center_index = (n - 1) // 2
    return center_index
if __name__ == '__main__':
    sample_data_ints = [3, 7, 5, 9]
    sample_data_floats = [1.1, 2.4, 3.8]
    result_1 = find_center_mark(sample_data_ints)
    print(f"Center index for integers: {result_1}")
    result_2 = find_center_mark(sample_data_floats)
    print(f"Center index for floats: {result_2}")