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
        pass
if __name__ == '__main__':
    data_generator = (f"item_{i}" for i in range(10**7))
    result = get_last_element(data_generator)
    print(f"The last element is: {result}")