from typing import Iterable, Tuple, Optional

def find_min_max(iterable: Iterable) -> Tuple[Optional[int], Optional[int]]:
    min_val = max_val = None
    for item in iterable:
        if min_val is None or item < min_val:
            min_val = item
        if max_val is None or item > max_val:
            max_val = item
    return (min_val, max_val)
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    print(find_min_max(sample_values))