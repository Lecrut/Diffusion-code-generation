def contains_special_chars(text):
    ascii_printable = set(chr(i) for i in range(32, 127))
    for char in text:
        if char not in ascii_printable:
            return True
    return False

if __name__ == '__main__':
    sample_string = "Hello World 123!"
    result = contains_special_chars(sample_string)
    print(result)