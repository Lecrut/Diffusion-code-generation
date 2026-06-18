from typing import TypeVar, Union, List, Tuple
T = TypeVar('T')
class IndexOutOfBoundsError(Exception):
    pass
class InvalidInputTypeError(TypeError):
    pass
def delete_at_index(sequence: Union[List[T], Tuple, str], index: int) -> Union[List[T], Tuple]:
    try:
        length = len(sequence)
    except TypeError:
        raise InvalidInputTypeError("Sequence must support indexing (e.g., list, tuple).") from None
    if not isinstance(index, int):
        raise InvalidInputTypeError("Index argument must be an integer.")
    if index < 0 or index >= length:
        raise IndexOutOfBoundsError(f"Invalid index {index}. Valid range is -{length} to {length-1} (or 0 to {length-1}).")
    if isinstance(sequence, str):
        return sequence[:index] + sequence[index+1:]
    elif isinstance(sequence, tuple):
        return [sequence[i] for i in range(length) if i != index]
    else:                                                                                                          
        new_list = list(sequence)
        del new_list[index]
        return new_list
if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry"]
    try:
        result = delete_at_index(sample_data, 1)
        print(f"Original List: {sample_data}")
        print(f"Modified List (removed index 1): {result}")
        sample_string = "Hello World!"
        result_str = delete_at_index(sample_string, 7)
        print(f"\nOriginal String: '{sample_string}'")
        print(f"Modified String (removed index 7): '{result_str}'")
    except IndexOutOfBoundsError as e:
        print(f"Index Error: {e}")
    try:
        delete_at_index(sample_data, -5)
    except IndexOutOfBoundsError as e:
        print(f"\nCaught expected Negative/Out of Range Error: {e}")
    sample_tuple = ("a", "b", "c")
    result_tuple_like = delete_at_index(sample_tuple, 0)
    print(f"Input Tuple converted to List after removal at index 0: {result_tuple_like}")