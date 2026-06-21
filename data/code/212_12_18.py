from typing import Iterable, Tuple, Optional

def min_max(iterable: Iterable[int]) -> Tuple[Optional[int], Optional[int]]:
    try:
        iterator = iter(iterable)
        first = next(iterator)
        min_val = max_val = first
        for value in iterator:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return (min_val, max_val)
    except StopIteration:
        return (None, None)
if __name__ == '__main__':
    print(min_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    print(min_max([]))
    print(min_max([-2, -5, -3]))