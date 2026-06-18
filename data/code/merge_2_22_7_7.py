from typing import Any, Union
def delete_at_index(sequence: list | tuple | str, index: int) -> None:
    if isinstance(sequence, str):
        raise ValueError("Strings cannot be deleted from directly due to immutability constraints.")
    elif isinstance(sequence, tuple):
        raise ValueError("Tuples cannot be deleted from directly due to immutability constraints.")
    elif not isinstance(sequence, list):
        raise TypeError(f"Unsupported sequence type: {type(sequence).__name__}. Only lists are supported for in-place deletion.")
    if index < 0 or index >= len(sequence):
        raise IndexError("Index out of range. Ensure it falls within [0, len(sequence)-1].")
    del sequence[index]
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    try:
        delete_at_index(sample_list, 2)
        print(f"Modified list after deletion at index 2: {sample_list}")
        string_input = "hello world"
        tuple_input = (10, 20, 30)
    except Exception as e:
        print(f"Error occurred during operation: {type(e).__name__}: {e}")