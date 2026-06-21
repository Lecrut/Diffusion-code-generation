from typing import Iterable, Tuple, Optional
EMPTY_INPUT = (None, None)

def find_min_max(iterable: Iterable) -> Tuple[Optional[int], Optional[int]]:
    try:
        iterator = iter(iterable)
        first = next(iterator)
        min_val = max_val = first
        for item in iterator:
            if item < min_val:
                min_val = item
            elif item > max_val:
                max_val = item
        return (min_val, max_val)
    except StopIteration:
        return EMPTY_INPUT
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_min_max(sample_values)
    print(f'Minimum: {result[0]}, Maximum: {result[1]}')