def get_or_set_value(data: list[int], index: int) -> tuple[list[int] | None, str]:
    if isinstance(index, bool):
        raise TypeError("Index must be an integer, boolean values are not allowed.")
    try:
        return data[index], f"Value at index {index} retrieved successfully."
    except IndexError as e:
        error_msg = f"Error: Index {index} is out of bounds for list of length {len(data)}."
        return None, error_msg
def set_value_in_slot(data: list[int], index: int, new_val: int) -> tuple[list[int] | None, str]:
    if isinstance(index, bool):
        raise TypeError("Index must be an integer, boolean values are not allowed.")
    try:
        data[index] = new_val
        return data, f"Value {new_val} set successfully at index {index}."
    except IndexError as e:
        error_msg = f"Error: Index {index} is out of bounds for list of length {len(data)}."
        return None, error_msg
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    retrieved_val, msg = get_or_set_value(sample_data, 2)
    print(f"Retrieval Result: {retrieved_val}, Message: {msg}")
    updated_list, set_msg = set_value_in_slot(sample_data.copy(), 0, 99)
    print(f"Set Operation Result: {updated_list}, Message: {set_msg}")
    retrieved_out_of_bounds, msg_oob = get_or_set_value(sample_data, -1)
    print(f"Out-of-Bounds Retrieval Result: {retrieved_out_of_bounds}, Message: {msg_oob}")