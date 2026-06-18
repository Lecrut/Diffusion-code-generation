from typing import Any, List, Tuple, Union
def append_element_to_sequence(sequence: Union[List[Any], Tuple[Any]], element: Any) -> None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        sequence.append(element)
    except AttributeError:
        raise ValueError("Tuples are immutable and cannot have elements appended directly. Use the provided function's logic for tuples instead of direct mutation if immutability is required, but this script assumes appendable sequences (lists).")
def add_element_to_tuple(sequence: Tuple[Any], element: Any) -> List[Any]:
    try:
        return list(sequence) + [element]
    except TypeError as e:
        raise ValueError(f"Invalid input type. Expected tuple or list, got {type(sequence).__name__}. Error details: {e}")
def append_element_to_sequence_safe(sequence: Union[List[Any], Tuple[Any]], element: Any) -> None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        sequence.append(element)
    except AttributeError:
        raise ValueError("Cannot append to tuples using 'append'. Convert list or use add_element_to_tuple.")
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    try:
        append_element_to_sequence(sample_list, "new_item")
        result_tuple = add_element_to_tuple(sample_tuple, 7)
    except Exception as e:
        print(f"Error occurred: {e}")