def get_string_at_position(string_list, position):
    if position < 0:
        return "Error: Position cannot be negative."
    if position >= len(string_list):
        return "Error: Position out of bounds."
    return string_list[position]
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print(get_string_at_position(sample_list, 0))
    print(get_string_at_position(sample_list, 2))
    print(get_string_at_position(sample_list, -1))
    print(get_string_at_position(sample_list, 4))