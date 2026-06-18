from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], elements_to_add: list[Any]) -> None:
    if not isinstance(lst, list) or len(elements_to_add) == 0:
        raise TypeError("First argument must be a non-empty list.")
    for item in elements_to_add:
        lst.append(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    new_elements = ['a', 'b']
    extend_list_end(sample_list, new_elements)