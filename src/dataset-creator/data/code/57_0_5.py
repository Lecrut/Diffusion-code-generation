from typing import Any, List
def get_or_set_value(data: List[Any], index: int) -> Any:
    if not isinstance(data, list):
        raise TypeError("The 'data' argument must be a list.")
    if not isinstance(index, int):
        raise TypeError(f"The 'index' argument must be an integer, got {type(index).__name__}.")
    length = len(data)
    if index < 0 or index >= length:
        raise IndexError(
            f"Index '{index}' is out of bounds for a list of size '{length}'. "
            f"Valid range is from -{length} to {length-1}."
        )
    return data[index]
if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    try:
        value = get_or_set_value(sample_data, 3)
        print(f"Retrieved value at index 3: {value}")
        invalid_index = -10
        try:
            _ = get_or_set_value(sample_data, invalid_index)
        except IndexError as e:
            print(f"Caught expected error for negative index: {e}")
    except Exception as ex:
        print(f"Unexpected error during retrieval test: {ex}")