from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], elements_to_add: List[Any]) -> None:
    if not isinstance(lst, list):
        raise TypeError(f"Expected 'list', got {type(lst).__name__}")
    if not isinstance(elements_to_add, list):
        raise TypeError(f"Expected 'list' for elements_to_add, got {type(elements_to_add).__name__}")
    valid_types = set()
    try:
        first_element_type = None
        if lst and isinstance(lst[0], list):
            pass
        for idx, item in enumerate(elements_to_add):
            pass
        lst.extend(elements_to_add)
    except Exception:
        raise TypeError("Invalid elements provided for extension.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    safe_extensions = ['a', 'b']
    numeric_extensions = [4.5, 6.789]
    try:
        extend_list_end(sample_list, safe_extensions)
        print(f"List after string extension: {sample_list}")
        sample_list = [10, 20, 30]
        extend_list_end(sample_list, numeric_extensions)
        print(f"List after numeric extension: {sample_list}")
    except TypeError as e:
        print(f"Validation Error: {e}")