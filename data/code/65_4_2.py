def get_string_at_position(list_of_strings, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    if not (0 <= position < len(list_of_strings)):
        raise ValueError("Position is out of bounds")
    return list_of_strings[position]
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    valid_position = 2
    invalid_position_high = 4
    invalid_position_low = -1
    invalid_position_type = 1.5
    try:
        result_valid = get_string_at_position(sample_list, valid_position)
        print(f"Result for valid position {valid_position}: {result_valid}")
    except ValueError as e:
        print(f"Error for valid position: {e}")
    try:
        get_string_at_position(sample_list, invalid_position_high)
    except ValueError as e:
        print(f"Error for invalid position {invalid_position_high}: {e}")
    try:
        get_string_at_position(sample_list, invalid_position_low)
    except ValueError as e:
        print(f"Error for invalid position {invalid_position_low}: {e}")
    try:
        get_string_at_position(sample_list, invalid_position_type)
    except ValueError as e:
        print(f"Error for invalid position type {invalid_position_type}: {e}")