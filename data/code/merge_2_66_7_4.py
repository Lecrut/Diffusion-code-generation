import sys
from typing import Iterable, Union
def max_weight_difference(*collections: list) -> int:
    all_elements = [elem for collection in collections for elem in collection]
    if not all_elements:
        return 0
    min_val = float('inf')
    max_val = float('-inf')
    for val in all_elements:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return max_val - min_val
if __name__ == '__main__':
    sample_data = [1, 5, 3], [-2, 8, 0]
    result = max_weight_difference(*sample_data)
    print(result)