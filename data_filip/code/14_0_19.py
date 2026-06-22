UNIQUE_CHAR_LIMIT = 256

def validate_string_input(data):
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    return data

def contains_unique_chars(text):
    validated_text = validate_string_input(text)
    if len(validated_text) > UNIQUE_CHAR_LIMIT:
        return False
    char_set = set()
    for current_char in validated_text:
        if current_char in char_set:
            return False
        char_set.add(current_char)
    return True

if __name__ == '__main__':
    sample_input = "abcdefg"
    output = contains_unique_chars(sample_input)
    print(output)