def get_string_at_position(string_list, position):
    if not (0 <= position < len(string_list)):
        raise ValueError("Invalid position")
    return string_list[position]
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    valid_position = 2
    invalid_position = 5
    try:
        result_valid = get_string_at_position(sample_list, valid_position)
        print(f"String at position {valid_position}: {result_valid}")
    except ValueError as e:
        print(f"Error for valid position: {e}")
    try:
        result_invalid = get_string_at_position(sample_list, invalid_position)
        print(f"String at position {invalid_position}: {result_invalid}")
    except ValueError as e:
        print(f"Error for invalid position: {e}")