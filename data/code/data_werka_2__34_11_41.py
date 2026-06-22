def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        return s
    FIRST_LETTER_INDEX = 0
    REST_OF_STRING_START = 1
    return s[FIRST_LETTER_INDEX].upper() + s[REST_OF_STRING_START:]

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "Python", "", "a"]
    for value in sample_values:
        print(capitalize_first_letter(value))