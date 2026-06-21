from typing import Iterable, Tuple, Optional

def min_max(iterable: Iterable) -> Tuple[Optional, Optional]:
    try:
        return min(iterable), max(iterable)
    except ValueError:
        return None, None

if __name__ == '__main__':
    print(min_max([3, 1, 4, 1, 5, 9, 2, 6]))
    print(min_max([]))
    print(min_max(['a', 'b', 'c']))