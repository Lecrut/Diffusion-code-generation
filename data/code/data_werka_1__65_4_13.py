def get_element_at_position(iterable, position):
    if not isinstance(position, int):
        raise ValueError("Position must be an integer")
    if position < 0:
        raise ValueError("Position cannot be negative")
    
    try:
        return next(iterable[pos] for pos in range(len(iterable)) if pos == position)
    except IndexError:
        raise ValueError("Position is out of bounds")

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    valid_position = 2
    invalid_position_high = 4
    invalid_position_low = -1

    try:
        result_valid = get_element_at_position(sample_list, valid_position)
        print(f"Result for valid position {valid_position}: {result_valid}")
    except ValueError as e:
        print(f"Error for valid position: {e}")

    try:
        result_invalid_high = get_element_at_position(sample_list, invalid_position_high)
        print(f"Result for invalid position {invalid_position_high}: {result_invalid_high}")
    except ValueError as e:
        print(f"Error for invalid position: {e}")

    try:
        result_invalid_low = get_element_at_position(sample_list, invalid_position_low)
        print(f"Result for invalid position {invalid_position_low}: {result_invalid_low}")
    except ValueError as e:
        print(f"Error for invalid position: {e}")