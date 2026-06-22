def print_characters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    for char in s:
        print(char)

if __name__ == '__main__':
    sample_string = 'Python'
    if isinstance(sample_string, str):
        print_characters(sample_string)