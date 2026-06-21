from typing import Iterable, Tuple, Optional

def find_extremes(iterable: Iterable) -> Tuple[Optional[int], Optional[int]]:
    iterator = iter(iterable)
    try:
        first = next(iterator)
        min_val = max_val = first
        for item in iterator:
            if item < min_val:
                min_val = item
            elif item > max_val:
                max_val = item
        return (min_val, max_val)
    except StopIteration:
        return (None, None)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_val, max_val = find_extremes(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")