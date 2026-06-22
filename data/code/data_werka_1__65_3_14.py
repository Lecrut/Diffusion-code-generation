def validate_position(strings, position):
    if not isinstance(position, int):
        raise TypeError("Position must be an integer")
    if position < 0 or position >= len(strings):
        raise ValueError("Invalid position")

def get_string_at_position(strings, position):
    validate_position(strings, position)
    return strings[position]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    position = 2
    try:
        result = get_string_at_position(sample_strings, position)
        print(result)
    except (ValueError, TypeError) as e:
        print(e)