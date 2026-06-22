def get_string_at_position(strings, position):
    MIN_POSITION = 0
    MAX_POSITION = len(strings) - 1
    
    if not isinstance(position, int):
        raise TypeError("Position must be an integer")
    
    if position < MIN_POSITION or position > MAX_POSITION:
        raise ValueError("Invalid position")
    
    return strings[position]

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    try:
        result = get_string_at_position(sample_strings, 2)
        print(result)
    except (ValueError, TypeError) as e:
        print(e)