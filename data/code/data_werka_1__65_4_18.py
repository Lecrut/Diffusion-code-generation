def get_string_at_position(list_of_strings, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    if position < 0 or position >= len(list_of_strings):
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
        print(f"String at position {valid_position}: {result_valid}")
    except ValueError as e:
        print(f"Error for valid position: {e}")

    try:
        result_invalid_high = get_string_at_position(sample_list, invalid_position_high)
        print(f"String at position {invalid_position_high}: {result_invalid_high}")
    except ValueError as e:
        print(f"Error for high invalid position {invalid_position_high}: {e}")

    try:
        result_invalid_low = get_string_at_position(sample_list, invalid_position_low)
        print(f"String at position {invalid_position_low}: {result_invalid_low}")
    except ValueError as e:
        print(f"Error for low invalid position {invalid_position_low}: {e}")

    try:
        result_invalid_type = get_string_at_position(sample_list, invalid_position_type)
        print(f"String at position {invalid_position_type}: {result_invalid_type}")
    except ValueError as e:
        print(f"Error for type invalid position {invalid_position_type}: {e}")