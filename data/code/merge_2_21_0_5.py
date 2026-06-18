from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def append_element(element: T, sequence: list[T]) -> None:
    if not isinstance(sequence, list):
        raise TypeError("Input must be a list.")
    sequence.append(element)
def extend_tuple(element: T, sequence: tuple[T, ...]) -> tuple[T, ...]:
    return (*sequence, element)
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    item_to_add: int = 4
    append_element(item_to_add, sample_list)
    sample_tuple = (5, 6, 7)
    new_tuple_result = extend_tuple(8, sample_tuple)
    print(f"Updated list: {sample_list}")
    print(f"New tuple result: {new_tuple_result}")