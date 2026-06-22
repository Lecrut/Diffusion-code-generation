def get_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    test_strings = [
        "Hello world",
        "   leading spaces and multiple words",
        "",
        "singleword",
        "  "
    ]
    for test_string in test_strings:
        print(f"Input: '{test_string}', Output: '{get_first_word(test_string)}'")