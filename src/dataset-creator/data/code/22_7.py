from typing import Any, Union
def delete_char_at_index(sequence: Union[str, list], index: int) -> None:
    if not isinstance(sequence, (str, list)):
        raise TypeError(f"'sequence' must be a str or list, got {type(sequence).__name__}")
    try:
        index = int(index)
    except ValueError as e:
        raise TypeError("Index argument must be an integer") from e
    if not isinstance(sequence[0], (str, list)):
        length = len(sequence)
        if index < 0 or index >= length:
            raise IndexError(f"Index {index} is out of range for sequence of length {length}")
    if isinstance(sequence, str):
        print(f"Cannot delete character at index {index} from immutable type '{type(sequence).__name__}'.")
    elif isinstance(sequence, list):
        del sequence[index]
if __name__ == '__main__':
    test_list = ['apple', 'banana', 'cherry']
    print(f"Original List: {test_list}")
    try:
        delete_char_at_index(test_list, 1)
        print(f"After deleting at index 1: {test_list}")
    except Exception as e:
        print(f"Error occurred while processing list: {e}")
    test_string = "Python Programming"
    print(f"\nOriginal String: '{test_string}'")
    try:
        delete_char_at_index(test_string, 7)
    except Exception as e:
        print(f"Error occurred while processing string: {e}")