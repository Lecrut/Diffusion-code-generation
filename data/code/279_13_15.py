def print_string_characters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    for char in s:
        print(char)

if __name__ == '__main__':
    sample_string = 'Python'
    print_string_characters(sample_string)