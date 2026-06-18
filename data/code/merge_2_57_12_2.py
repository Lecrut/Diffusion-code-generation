from typing import Sequence, TypeVar
T = TypeVar('T')
def get_element_at_index(sequence: Sequence[T], index: int) -> T:
    return sequence[index]
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30, 40, 50]
    sample_tuple: tuple[str, ...] = ("apple", "banana", "cherry")
    index_to_access: int = 2
    result_from_list: int | None = get_element_at_index(sample_list, index_to_access) if len(sample_list) > index_to_access else None
    print(f"Element at {index_to_access} in list: {result_from_list}")
    try:
        result_from_tuple: str = get_element_at_index(sample_tuple, 1)
        print(f"Element at {index_to_access} in tuple: '{result_from_tuple}'")
    except IndexError as e:
        print(f"IndexError occurred for tuple access: {e}")
    try:
        get_element_at_index(sample_list, 10)
    except IndexError:
        pass