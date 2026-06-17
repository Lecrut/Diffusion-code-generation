from typing import Iterable, Any
def get_first_element(iterable: Iterable[Any]) -> Any:
    try:
        return next(iter(iterable))
    except StopIteration:
        raise IndexError("Iterable is empty")
if __name__ == '__main__':
    data = [10, 20, 30]
    first_item = get_first_element(data)
    print(first_item)