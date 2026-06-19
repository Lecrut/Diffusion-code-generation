def find_repeated_letters(input_string):
    char_map = {}
    for char in input_string:
        if char.isalpha():
            lower_char = char.lower()
            char_map[lower_char] = char_map.get(lower_char, 0) + 1
    repeated_chars = [char for char, count in char_map.items() if count > 1]
    return repeated_chars

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    result = find_repeated_letters(sample_input)
    print(result)