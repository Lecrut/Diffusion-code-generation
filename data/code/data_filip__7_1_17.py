def has_special_characters(text):
    special_chars_found = False
    for char in text:
        ascii_val = ord(char)
        is_letter = 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122
        is_digit = 48 <= ascii_val <= 57
        is_space = ascii_val == 32
        if not is_letter and not is_digit and not is_space:
            special_chars_found = True
            break
    return special_chars_found

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello@World",
        "123456",
        "Test!@#",
        "Clean_String",
        "",
        "   ",
        "Mixed123!"
    ]

    for sample in sample_strings:
        result = has_special_characters(sample)
        print(f"String: '{sample}' -> Has special characters: {result}")