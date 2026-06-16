import threading
from typing import Iterable, TypeVar, Any
T = TypeVar('T')
def append_element(iterable: Iterable[T], element: T) -> list[T]:
    result_list = list(iterable)
    return result_list + [element]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    modified_data = append_element(sample_data, "new")
    print(modified_data)