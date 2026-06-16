from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list_end(lst: List[T], elements_to_add: List[Any]) -> None:
    if not isinstance(lst, list):
        raise TypeError(f"Expected a list instance, got {type(lst).__name__}")
    current_len = len(lst)
    for idx, new_elem in enumerate(elements_to_add):
        try:
            lst[current_len + idx] = new_elem
        except IndexError:
            raise ValueError(f"List size mismatch during extension attempt.")
def main():
    sample_list: List[int | str] = [1, 2, 3]
    elements_to_append: List[Any] = ["a", "b", 4.5]
    try:
        extend_list_end(sample_list, elements_to_append)
        print(f"Extended list: {sample_list}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred during extension: {e}")
if __name__ == '__main__':
    main()