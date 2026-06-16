from typing import Any, Union
def delete_at_index(sequence: list[Any], index: int) -> None:
    if not isinstance(sequence, list):
        raise TypeError(f"Expected a 'list' object but received {type(sequence).__name__}")
    try:
        index = int(index)
    except (TypeError, ValueError):
        raise TypeError("The second argument must be an integer or convertible to one.")
    if not (-len(sequence) <= index < len(sequence)):
        raise IndexError(f"Index {index} is out of range for a list of length {len(sequence)}")
    del sequence[index]
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    delete_at_index(sample_data, 1)
    print(f"Modified list: {sample_data}")