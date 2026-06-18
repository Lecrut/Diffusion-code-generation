def safe_reverse_iterate(data: list[int]) -> None:
    length = len(data)
    if not isinstance(data, (list)):
        raise TypeError("Input must be a list of integers.")
    try:
        for i in range(-length, 0):
            value = data[i]
            if not isinstance(value, int):
                raise TypeError(f"Element at index {i} must be an integer.")
    except IndexError as e:
        raise IndexError("Attempted to access a position outside the list bounds.") from e
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        safe_reverse_iterate(sample_data)
        length = len(sample_data)
        for i in range(-length, 0):
            print(f"Index {i}: Value {sample_data[i]}")
    except (TypeError, IndexError) as exception:
        error_message = f"{type(exception).__name__} occurred: {exception}"
        raise Exception(error_message) from exception