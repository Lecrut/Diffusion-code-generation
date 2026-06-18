def get_or_set_value(data: list[int], index: int, value=None) -> int | None:
    if not isinstance(data, list):
        raise TypeError("The 'data' argument must be a list.")
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError("The 'index' argument must be an integer.")
    try:
        return data[index] if value is None else (value, index)
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds for the list with length {len(data)}.") from e
if __name__ == '__main__':
    sample_data = [100, 200, 300]
    retrieved_value = get_or_set_value(sample_data, 1)
    print(f"Retrieved value at index 1: {retrieved_value}")
    set_result = get_or_set_value(sample_data, 2, 999)
    if isinstance(set_result, tuple):
        _, idx = set_result
        print(f"Set result (index updated to {idx}): Value at index 2 is now {sample_data[2]}")
    try:
        get_or_set_value(sample_data, -5)
    except IndexError as e:
        print(f"Caught expected error for negative/out-of-range index: {e}")
    invalid_index = "123"                         
    try:
        get_or_set_value(sample_data, invalid_index)
    except TypeError as e:
        print(f"Caught expected error for non-integer index: {e}")