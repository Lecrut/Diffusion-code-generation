def get_string_at_position(strings, position):
    if not (0 <= position < len(strings)):
        raise ValueError("Invalid position")
    return strings[position]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    positions_to_test = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3
    }
    
    try:
        position_key = 'second'
        result = get_string_at_position(sample_strings, positions_to_test[position_key])
        print(f"The string at the {position_key} position is: {result}")
    except ValueError as e:
        print(e)