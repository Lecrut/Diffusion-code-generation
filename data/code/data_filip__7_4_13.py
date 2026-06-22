def first_special_char(s):
    import string
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "hello, world!",
        "no special chars here",
        "@start with special",
        "12345",
        ""
    ]
    for s in sample_strings:
        result = first_special_char(s)
        print(f"'{s}' -> {result}")