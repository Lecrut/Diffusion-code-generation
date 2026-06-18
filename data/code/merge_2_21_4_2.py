from collections import deque
import sys
def append_elements(collection: list | tuple, elements) -> None:
    if not isinstance(elements, (list, tuple)):
        raise TypeError("elements must be a list or tuple")
    for item in elements:
        collection.append(item)
if __name__ == '__main__':
    data = [10]
    append_elements(data, [20, 30])