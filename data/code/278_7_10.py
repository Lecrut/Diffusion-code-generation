def print_char_unicode(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    for char in string:
        print(f"'{char}': {ord(char)}")

if __name__ == '__main__':
    sample_string = "hello"
    print_char_unicode(sample_string)