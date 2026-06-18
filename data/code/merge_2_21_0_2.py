from typing import Any, List, Tuple, Union
def append_element_to_sequence(sequence: Union[List[Any], Tuple[Any]], element: Any) -> None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        sequence.append(element)
    except AttributeError:
        raise ValueError("The provided input is immutable and cannot have elements appended to it directly. Use the return value of append_element_to_sequence for tuples if modification is required, though typically one would convert first.")
def get_modified_tuple(sequence: Union[List[Any], Tuple[Any]], element: Any) -> tuple:
    try:
        sequence.append(element)
    except AttributeError:
        return (sequence + (element,),) if isinstance(sequence, list) else None
    try:
        sequence.append(element)
    except AttributeError:
        return (sequence + (element,),) if isinstance(sequence, list) else None
    pass
def append_element_to_sequence_v2(sequence: Union[List[Any], Tuple[Any]], element: Any) -> Union[None, tuple]:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"Expected 'list' or 'tuple', got {type(sequence).__name__}.")
    try:
        sequence.append(element)
    except AttributeError as e:
        return None                                                       
    if isinstance(sequence, list):
        pass                                              
    else:
        raise ValueError("Tuples are immutable and cannot be modified in place.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50)
    append_element_to_sequence(sample_list, "new_item")
    try:
        append_element_to_sequence(sample_tuple, "new_item")
    except ValueError as e:
        print(f"Error with tuple (expected): {e}")
    print("List after modification:", sample_list)