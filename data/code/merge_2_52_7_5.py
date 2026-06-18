import sys
from typing import Iterable, TypeVar
T = TypeVar('T')
def get_last_element(iterable: Iterable[T]) -> T | None:
    iterator = iter(iterable)
    try:
        last_item = next(iterator)
        while True:
            item = next(iterator)
            last_item = item
        return last_item
    except StopIteration:
        return None
if __name__ == '__main__':
    large_data_generator = (f"item_{i}" for i in range(10_000))
    result = get_last_element(large_data_generator)
    print(result)