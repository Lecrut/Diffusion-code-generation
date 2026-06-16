from typing import Any, Union
def delete_at_index(sequence: list | tuple | str, index: int) -> None:
    supported_types = (list, tuple)
    if not isinstance(sequence, supported_types):
        raise TypeError(f"Unsupported sequence type: {type(sequence).__name__}. Only list and tuple are allowed.")
    try:
        length = len(sequence)
    except Exception as e:
        raise TypeError(f"Sequence does not support length calculation. Error: {e}") from None
    if isinstance(index, int):
        pass                                                                            
    else:
        raise TypeError("Index must be an integer.")
    try:
        del sequence[index]
    except IndexError as e:
        raise IndexError(f"Position {index} is out of bounds. Length: {length}") from None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        delete_at_index(sample_list, 2)
        print(f"Modified list after deleting index 2: {sample_list}")
        sample_tuple = (1, 2, 3)
        try:
            delete_at_index(sample_tuple, -5)
        except IndexError as e:
            print(f"Caught expected error for tuple index out of bounds: {e}")
    except Exception as ex:
        print(f"Unexpected exception occurred: {ex}")