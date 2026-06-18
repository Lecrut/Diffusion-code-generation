import threading
from typing import Any, Iterable, TypeVar
T = TypeVar('T')
def append_element(iterable: Iterable[T], element: T) -> list[T]:
    result_list = list(iterable)
    return result_list + [element]
if __name__ == '__main__':
    sample_iterable = [1, 2, 3]
    appended_result = append_element(sample_iterable, 'extra')
    print(appended_result)