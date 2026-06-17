from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def get_first_item(items: Iterable[T]) -> T:
    if items is None or not isinstance(items, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        return next(iter(items))
    except StopIteration:
        raise ValueError("The provided iterable is empty.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_item(sample_list)
    print(result)
    try:
        get_first_item([])
    except ValueError as e:
        print(f"Error for empty list: {e}")
    try:
        get_first_item(None)
    except TypeError as e:
        print(f"Error for None input: {e}")