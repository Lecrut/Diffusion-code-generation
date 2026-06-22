def remove_spaces(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ''.join(c for c in s if c != ' ')

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(remove_spaces(sample_string))