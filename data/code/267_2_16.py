def is_long_word(text):
    if not isinstance(text, str) or text == "":
        return False
    return len(text) > 20

if __name__ == '__main__':
    sample1 = "This is a short sentence"
    sample2 = "This is a very long sentence that definitely exceeds twenty characters"
    sample3 = ""
    sample4 = 12345

    print(f"'{sample1}' is long: {is_long_word(sample1)}")
    print(f"'{sample2}' is long: {is_long_word(sample2)}")
    print(f"Empty string is long: {is_long_word(sample3)}")
    print(f"Non-string input (integer): {is_long_word(sample4)}")