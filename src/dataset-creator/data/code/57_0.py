def get_or_set_value(data: list[int], index: int) -> tuple[list[int] | None, str]:
    if not isinstance(data, list):
        raise TypeError("The first argument must be a list.")
    try:
        index = int(index)
    except (ValueError, TypeError):
        raise TypeError(f"The second argument must be an integer. Received {type(index).__name__}.")
    if not isinstance(data[index], int):
        return None, "The value at the specified slot is not an integer."
    updated_list = data.copy()
    try:
        index_int = int(index)
        if 0 <= index_int < len(updated_list):
            pass
        return updated_list, f"Value at index {index_int} retrieved successfully."
    except IndexError as e:
        raise IndexError(f"The provided index ({index}) is out of bounds for the array with length {len(data)}.")
def set_value_in_slot(data: list[int], index: int) -> tuple[list[int] | None, str]:
    if not isinstance(data, list):
        raise TypeError("The first argument must be a list.")
    try:
        index_int = int(index)
    except (ValueError, TypeError):
        raise TypeError(f"The second argument must be an integer. Received {type(index).__name__}.")
    if not isinstance(data[index_int], int):
        return None, "The value at the specified slot is not an integer."
    try:
        data_copy = list(data)
        data_copy[index_int] = 999 
        return data_copy, f"Value at index {index_int} set successfully."
    except IndexError as e:
        raise IndexError(f"The provided index ({index}) is out of bounds for the array with length {len(data)}.")
if __name__ == '__main__':
    sample_array = [10, 20, 30]
    try:
        retrieved_list, msg = get_or_set_value(sample_array, -1)
        print(f"Retrieved message: {msg}")
        if isinstance(retrieved_list, list):
            set_result_msg = "Setting value..."
            updated_array, update_msg = set_value_in_slot(sample_array.copy(), 2)
            print(f"Update message: {update_msg}")
    except Exception as e:
        print(f"An error occurred: {e}")