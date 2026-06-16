from typing import TypeVar, List, Iterable, Union
T = TypeVar('T')
def extend_list(
    lst: List[T], 
    elements_to_add: Iterable[T]
) -> None:
    for item in elements_to_add:
        if not isinstance(item, type(lst[0]) if lst else object):
            raise TypeError(f"Expected element of type {type(lst[0]).__name__} if list is non-empty.")
        try:
            lst.append(item)
        except Exception as e:
            print(f"Error appending item: {e}")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    new_elements = [4.0, "five", True]
    try:
        extend_list(sample_list, new_elements)
        print(f"Extended list: {sample_list}")
    except TypeError as e:
        print(e)