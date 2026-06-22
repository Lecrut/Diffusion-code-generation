def has_no_special_chars(text):
    return text.isalnum() or text == ""

if __name__ == '__main__':
    sample_strings = [
        "hello123",
        "hello!world",
        "12345",
        "abc def",
        ""
    ]
    for s in sample_strings:
        print(has_no_special_chars(s))