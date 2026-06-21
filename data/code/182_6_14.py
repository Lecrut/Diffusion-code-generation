def separate_chars_by_ord(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return [ord(c) for c in s]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    try:
        result = separate_chars_by_ord(sample_string)
        print(result)
    except ValueError as e:
        print(e)