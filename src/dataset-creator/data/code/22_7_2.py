from typing import Any, Union
def delete_at_index(sequence: list | tuple | str, index: int) -> None:
    if isinstance(sequence, str):
        raise TypeError("Strings are immutable; cannot delete character in-place.")
    elif isinstance(sequence, tuple):
        raise TypeError("Tuples are immutable; cannot remove element in-place.")
    try:
        del sequence[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds for the provided sequence length ({len(sequence)}).") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    try:
        delete_at_index(sample_list, 2)
        print(f"Modified list: {sample_list}")
    except IndexError as ex:
        print(f"IndexError occurred: {ex}")
    sample_tuple = (1, 2, 3)
    try:
        delete_at_index(sample_tuple, 0)
    except TypeError as te:
        print(f"TypeError for tuple deletion: {te}")
    sample_str = "hello"
    try:
        delete_at_index(sample_str, 1)
    except TypeError as ts:
        print(f"TypeError for string deletion: {ts}")