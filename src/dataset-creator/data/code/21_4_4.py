from collections import deque
import sys
def append_elements(collection: list | tuple | set) -> None:
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Collection must be a list or tuple.")
    new_items = [10, 20, 30]
    collection.extend(new_items)
if __name__ == '__main__':
    data = deque([5]) if isinstance(deque.__init__, type(lambda: None)) else []                                             
    try:
        append_elements(data)
    except Exception as e:
        print(f"Error: {e}")