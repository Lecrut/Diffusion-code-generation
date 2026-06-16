import threading
from typing import Any, Iterable, List
def append_element(iterable: Iterable[Any], element: Any) -> List[Any]:
    result = []
    for item in iterable:
        result.append(item)
    result.append(element)
    return result
if __name__ == '__main__':
    data_list = [1, 2, 3]
    modified_data = append_element(data_list, 'extra')
    print(modified_data)