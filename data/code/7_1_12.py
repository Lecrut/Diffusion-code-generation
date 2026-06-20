def has_special_characters(text):
    special_ranges = [
        (33, 47),
        (58, 64),
        (91, 96),
        (123, 126)
    ]
    for char in text:
        char_code = ord(char)
        for start, end in special_ranges:
            if start <= char_code <= end:
                return True
    return False

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "hello!",
        "world?",
        "12345",
        "test@123",
        ""
    ]
    for s in sample_strings:
        result = has_special_characters(s)
        print(result)