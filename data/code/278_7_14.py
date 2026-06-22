def print_unicode_codepoints(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    for char in s:
        print(f"{char}: {ord(char)}")

if __name__ == '__main__':
    sample_string = "hello world"
    print_unicode_codepoints(sample_string)