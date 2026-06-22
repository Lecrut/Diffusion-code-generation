def print_unicode_chars(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    for char in input_string:
        print(f"'{char}': {ord(char)}")

if __name__ == '__main__':
    sample_string = "hello"
    print_unicode_chars(sample_string)