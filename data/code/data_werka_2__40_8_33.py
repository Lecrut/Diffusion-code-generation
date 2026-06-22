def print_first_letters(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings.")
    for string in strings:
        if not isinstance(string, str):
            raise ValueError("All elements in the list must be strings.")
        if string:
            print(string[0])

if __name__ == '__main__':
    sample_strings = ['grape', 'honeydew', 'kiwi', 'lemon']
    try:
        print_first_letters(sample_strings)
    except ValueError as e:
        print(e)