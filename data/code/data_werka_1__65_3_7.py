def get_string_at_position(strings, position):
    if position < 0 or position >= len(strings):
        raise ValueError("Invalid position")
    return strings[position]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    position_map = {
        'first': 0,
        'second': 1,
        'third': 2
    }
    
    try:
        position_key = 'second'
        result = get_string_at_position(sample_strings, position_map[position_key])
        print(result)
    except ValueError as e:
        print(e)