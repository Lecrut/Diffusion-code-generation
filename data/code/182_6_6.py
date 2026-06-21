def separate_chars_by_ord(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return [ord(c) for c in input_string]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(separate_chars_by_ord(sample_string))