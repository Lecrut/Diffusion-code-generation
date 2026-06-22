def capitalize_first_letter(input_string):
    if not input_string:
        return input_string
    first = input_string[0]
    if not first.isalpha():
        if input_string[1:].isupper():
            return input_string
        return input_string
    return first.upper() + input_string[1:]

if __name__ == '__main__':
    test_strings = ["hello", "h", "", "world", "café", "über", "πi", "123abc", "   spaced", "ALREADY Capitalized"]
    for s in test_strings:
        print(capitalize_first_letter(s))