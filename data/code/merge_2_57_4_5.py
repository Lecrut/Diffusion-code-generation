def safe_reverse_iterate(data: list[int]) -> None:
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    for item in data:
        if not isinstance(item, int) or isinstance(item, bool):
            raise ValueError(f"List contains unsupported type {type(item).__name__}. Only integers are allowed.")
    length = len(data)
    current_index = -1
    try:
        while True:
            if not isinstance(current_index, int):
                raise TypeError("Index must be an integer.")
            value = data[current_index]
            if current_index < -length or current_index > 0:
                raise IndexError(f"Index {current_index} is out of range.")
            print(value)
            current_index -= 1
    except TypeError as te:
        if "index must be an integer" in str(te):
            raise
        else:
            raise
    except IndexError as ie:
        print(f"Error accessing position {ie.args[0]}")
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    try:
        safe_reverse_iterate(sample_data)
    except (TypeError, ValueError, IndexError):
        print("An error occurred during iteration.")