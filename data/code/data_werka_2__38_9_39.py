def find_repeated_letters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def is_alpha_lower(char):
        return char.isalpha() and char.lower()
    
    seen_letters = set()
    repeated_letters = set()
    
    for char in input_string:
        lower_char = char.lower()
        if is_alpha_lower(lower_char):
            if lower_char in seen_letters:
                repeated_letters.add(lower_char)
            else:
                seen_letters.add(lower_char)
    
    return list(repeated_letters)

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    try:
        result = find_repeated_letters(sample_input)
        print(result)
    except ValueError as e:
        print(e)