from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], elements_to_add: list[Any]) -> None:
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    for item in elements_to_add:
        lst.append(item)
if __name__ == '__main__':
    original_list = [10, 20, 30]
    new_elements = [40, 50, 60]
    try:
        extend_list_end(original_list, new_elements)
        print(f"Extended List: {original_list}")
    except TypeError as e:
        print(f"Error: {e}")