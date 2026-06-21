from typing import Iterable, Tuple, Optional

def find_min_max(iterable: Iterable[int]) -> Tuple[Optional[int], Optional[int]]:
    min_val = None
    max_val = None
    for element in iterable:
        if min_val is None or element < min_val:
            min_val = element
        if max_val is None or element > max_val:
            max_val = element
    return (min_val, max_val)
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_max(sample_values))