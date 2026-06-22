from typing import Tuple, List, TypeVar

T = TypeVar('T')

def fetch_extremes(sequence: List[T]) -> Tuple[T, T]:
    limit = len(sequence)
    if limit == 0:
        raise ValueError("Empty sequence")
    if limit == 1:
        item = sequence[0]
        return item, item
    return sequence[0], sequence[-1]

if __name__ == '__main__':
    items = [7, 1, 9, 3]
    result = fetch_extremes(items)
    print(result)