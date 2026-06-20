def contains_special_characters(input_string):
    for char in input_string:
        ascii_val = ord(char)
        if 32 <= ascii_val <= 126:
            if not char.isalnum() and (not char.isspace()):
                return True
    return False
if __name__ == '__main__':
    sample_strings = ['Hello World', 'Hello@World!', '12345', 'no_special_chars_here', 'has#special$chars%', '   spaces   ', 'Mixed123!@#']
    for test_string in sample_strings:
        result = contains_special_characters(test_string)
        print(f"String: '{test_string}' -> Contains special characters: {result}")