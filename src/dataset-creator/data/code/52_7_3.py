import sys
from typing import Iterable, TypeVar
T = TypeVar('T')
def get_last_element(data: Iterable[T]) -> T | None:
    iterator = iter(data)
    try:
        item = next(iterator)
        while True:
            new_item = next(iterator)
            item = new_item
        return item
    except StopIteration:
        pass
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5] * 10000
    result = get_last_element(sample_data)
    print(result)