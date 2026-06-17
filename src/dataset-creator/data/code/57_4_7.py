def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    for item in data:
        if isinstance(item, float) or not isinstance(item, int):
            raise TypeError(f"Unsupported type '{type(item).__name__}' found at index {data.index(item)}")
    for i in range(-1, -(len(data)), -1):
        try:
            value = data[i]
            if not isinstance(value, int):
                raise TypeError(f"Element at index {i} is not an integer.")
        except IndexError as e:
            raise IndexError("Attempted to access a position outside valid bounds." + str(e))
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    try:
        _ = sample_data[5.5]                                                               
    except TypeError as e:
        print(f"Caught expected error during validation: {e}")
    safe_reverse_iterate(sample_data)