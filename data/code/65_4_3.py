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
        result1 = get_string_at_position(sample_list, valid_position)
        print(f"Result at position {valid_position}: {result1}")
    except ValueError as e:
        print(f"Error for valid position: {e}")
    try:
        result2 = get_string_at_position(sample_list, invalid_position_high)
        print(f"Result at position {invalid_position_high}: {result2}")
    except ValueError as e:
        print(f"Error for invalid position {invalid_position_high}: {e}")
    try:
        result3 = get_string_at_position(sample_list, invalid_position_low)
        print(f"Result at position {invalid_position_low}: {result3}")
    except ValueError as e:
        print(f"Error for invalid position {invalid_position_low}: {e}")
    try:
        result4 = get_string_at_position(sample_list, invalid_position_type)
        print(f"Result at position {invalid_position_type}: {result4}")
    except ValueError as e:
        print(f"Error for invalid position type {invalid_position_type}: {e}")