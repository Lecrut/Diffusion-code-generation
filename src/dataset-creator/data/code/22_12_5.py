def remove_by_index(container: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if container is None:
        raise ValueError("Container cannot be null.")
    try:
        length = len(container)
    except TypeError as e:
        raise TypeError(f"Input type {type(container).__name__} does not support length operation.") from e
    if index < 0 or index >= length:
        raise IndexError(f"Index out of range. Valid indices are between -{length} and {length-1}.")
    try:
        container[index] = None
    except (TypeError, AttributeError) as e:
        raise TypeError("Cannot modify the provided object.") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    remove_by_index(sample_list, target_index)
    print(f"Updated list: {sample_list}")