from typing import Union, List, Tuple, Any
def append_element_to_sequence(sequence: Union[List[Any], Tuple[Any]], element: Any) -> bool:
    if isinstance(sequence, list):
        sequence.append(element)
        return True
    elif isinstance(sequence, tuple):
        try:
            new_list = [element] + list(sequence)
            return False                                                                                                      
        except TypeError:
            raise ValueError("Input must be a valid sequence (list or tuple).")
def main():
    sample_lists: List[Union[List[Any], Tuple[Any]]] = [
        ([1, 2, 3], "new_item"),
        ((4, 5, 6), "tuple_element"),
    ]
    for seq, item in sample_lists:
        try:
            result = append_element_to_sequence(seq, item)
            print(f"Input type: {type(seq).__name__}, Result of operation: {result}")
            if isinstance(seq, list):
                print(f"Modified List: {seq}")
            else:
                pass
        except ValueError as e:
            print(f"Error with input type {type(seq).__name__}: {e}")
if __name__ == '__main__':
    main()