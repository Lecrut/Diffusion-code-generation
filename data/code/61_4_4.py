def get_string_at_position(strings, position):
    if position < 0:
        return "Error: Position is negative."
    try:
        return strings[position]
    except IndexError:
        return "Error: Position out of range."

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    position = -1
    result = get_string_at_position(sample_strings, position)
    print(result)