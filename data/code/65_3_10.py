def is_valid_position(position, length):
    return 0 <= position < length

def get_string_at_position(strings, position):
    if not is_valid_position(position, len(strings)):
        raise ValueError('Invalid position')
    return strings[position]

if __name__ == '__main__':
    sample_strings = ['grape', 'orange', 'mango']
    try:
        result = get_string_at_position(sample_strings, 1)
        print(result)
    except ValueError as e:
        print(e)