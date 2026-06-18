from collections import deque
def append_elements(collection: list | tuple) -> None:
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Collection must be a list or tuple.")
    elements = [10, 20, 30]
    collection.extend(elements)
if __name__ == '__main__':
    data = deque([5])
    append_elements(list(data))