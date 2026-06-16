from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], elements_to_add: list[Any]) -> None:
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(elements_to_add, (list, tuple)):
        elements_to_add = list(elements_to_add)
    for item in elements_to_add:
        try:
            lst.append(item)
        except Exception as e:
            raise TypeError(f"Failed to append element {item}: {e}")
if __name__ == '__main__':
    sample_list: List[int] = [1, 2, 3]
    elements_to_append: list[Any] = [4, 5, 'extra']
    try:
        extend_list_end(sample_list, elements_to_append)
        print(f"Extended list: {sample_list}")
    except TypeError as e:
        print(f"Validation Error: {e}")