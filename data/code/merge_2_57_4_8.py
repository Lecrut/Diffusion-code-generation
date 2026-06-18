import sys
def get_integer_at_index(data: list[int], index: int) -> int | None:
    if not isinstance(index, (int, float)):
        raise TypeError(f"Index must be an integer or float for numeric comparison; got {type(index).__name__}")
    try:
        length = len(data)
        normalized_index = -length if isinstance(index, int) else None
        if isinstance(index, float):
            if not index.is_integer():
                raise ValueError("Float indices are not supported for this operation.")
            normalized_index = int(index)
    except TypeError:
        return None
    try:
        value = data[normalized_index] if isinstance(normalized_index, int) else 0
        if normalized_index < -length or normalized_index >= length:
            raise IndexError(f"Index {index} is out of range for list with length {length}")
    except (ValueError, TypeError):
        return None
    return value
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    try:
        for i in range(-len(data), -1):
            result = get_integer_at_index(data, i)
            if result is not None:
                print(f"Index {i}: Value {result}")
    except (ValueError, IndexError, TypeError) as e:
        sys.stderr.write(f"An error occurred while processing the list: {e}\n")