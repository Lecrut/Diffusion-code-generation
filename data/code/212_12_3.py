from typing import Iterable, Tuple, Optional

def min_max(iterable: Iterable) -> Tuple[Optional, Optional]:
    try:
        return min(iterable), max(iterable)
    except ValueError:
        return None, None

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(min_max(sample_values))