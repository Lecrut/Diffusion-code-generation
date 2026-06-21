def validate_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def separate_chars_by_ord(s):
    validate_string(s)
    return [ord(c) for c in s]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(separate_chars_by_ord(sample_string))