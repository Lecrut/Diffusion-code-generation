def get_string_at_position(iterable, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    if position < 0:
        raise ValueError("Position cannot be negative")
    
    index = 0
    for element in iterable:
        if index == position:
            return element
        index += 1
    
    raise ValueError("Position is out of bounds")

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
        result_invalid_high = get_string_at_position(sample_list, invalid_position_high)
        print(f"Result for invalid high position {invalid_position_high}: {result_invalid_high}")
    except ValueError as e:
        print(f"Error for invalid high position: {e}")
    
    try:
        result_invalid_low = get_string_at_position(sample_list, invalid_position_low)
        print(f"Result for invalid low position {invalid_position_low}: {result_invalid_low}")
    except ValueError as e:
        print(f"Error for invalid low position: {e}")
    
    try:
        result_invalid_type = get_string_at_position(sample_list, invalid_position_type)
        print(f"Result for invalid type position {invalid_position_type}: {result_invalid_type}")
    except ValueError as e:
        print(f"Error for invalid type position: {e}")