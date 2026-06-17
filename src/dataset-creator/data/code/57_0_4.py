def get_or_set_value(data: list[int], index: int) -> tuple[list[int] | None, str]:
    try:
        if isinstance(index, int) and not isinstance(index, bool):
            return data[index], ""
        else:
            error_msg = f"Index must be a valid integer (not {type(index).__name__})."
            return None, error_msg
    except IndexError as e:
        error_msg = str(e).replace("index out of range", "Value is outside the bounds of the array.")
        return None, error_msg
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result, msg = get_or_set_value(sample_data, 2)
    if not isinstance(result, int):
        print(f"Error retrieving value at index {2}: {msg}")
    else:
        sample_data[2] = 999
        result_check, msg_check = get_or_set_value(sample_data, 3)
        if not isinstance(result_check, int):
            print(f"Error retrieving updated value at index {3}: {msg_check}")
        else:
            _, out_of_bounds_msg = get_or_set_value(sample_data, -10)
            print(f"Out of bounds message for negative large index: '{out_of_bounds_msg}'")
    invalid_result, invalid_type_msg = get_or_set_value(sample_data, "5")
    if not isinstance(invalid_result, list):
        print(f"Error due to non-integer index '{invalid_type_msg}'")