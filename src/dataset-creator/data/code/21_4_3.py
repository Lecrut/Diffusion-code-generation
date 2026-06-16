from collections import deque as _deque_
def append_elements(collection: list | tuple, *elements) -> None:
    if not isinstance(elements[0], (int, float, str)):
        raise TypeError("Elements must be basic types")
    for el in elements:
        collection.append(el)
if __name__ == '__main__':
    data = [1]
    append_elements(data, "a", 2.5, True)