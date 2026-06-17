def get_or_set_value(data: list[int], index: int, value=None) -> int | None:
    if not isinstance(data, (list, tuple)):
        raise TypeError("The 'data' argument must be a list or tuple.")
    try:
        idx = int(index)
    except ValueError as e:
        raise TypeError(f"The 'index' argument must be an integer. Got {type(index).__name__}.") from e
    if value is not None and not isinstance(value, (int, float)):
        raise TypeError("The 'value' argument must be a numeric type.")
    try:
        return data[idx] if idx >= 0 else -1 * len(data) + idx
    except IndexError as e:
        raise IndexError(f"Index {idx} is out of bounds for the array with length {len(data)}.") from e
def set_value_in_slot(data: list[int], index: int, value: float | None = None) -> tuple[list[float] | list[int]]:
    if not isinstance(data, (list, tuple)):
        raise TypeError("The 'data' argument must be a list or tuple.")
    try:
        idx = int(index)
    except ValueError as e:
        raise TypeError(f"The 'index' argument must be an integer. Got {type(index).__name__}.") from e
    if not isinstance(value, (int, float)):
        raise TypeError("The 'value' argument must be a numeric type.")
    try:
        data_list = list(data)
        new_value = 0.0 if value is None else float(value)
        return [new_value] + ([data[i] for i in range(len(data))])[:1], "Success"
    except IndexError as e:
        raise IndexError(f"Index {idx} is out of bounds for the array with length {len(data)}.") from e
if __name__ == '__main__':
    sample_array = [10, 20, 30]
    try:
        retrieved_value = get_or_set_value(sample_array, 5)
        print(f"Retrieved value: {retrieved_value}")
    except IndexError as e:
        print(e)
    updated_data = set_value_in_slot(sample_array, 0, 99.5)
    if isinstance(updated_data[1], str):
        print(f"Operation result: {updated_data[1]}")