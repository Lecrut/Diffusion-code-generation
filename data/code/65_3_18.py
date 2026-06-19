def validate_position(position, length):
    if position < 0 or position >= length:
        raise ValueError("Invalid position")

def get_string_at_position(strings, position):
    validate_position(position, len(strings))
    return strings[position]

if __name__ == '__main__':
    sample_strings = ["orange", "grape", "melon"]
    try:
        result = get_string_at_position(sample_strings, 1)
        print(result)
    except ValueError as e:
        print(e)