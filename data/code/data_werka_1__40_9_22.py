def extract_first_letters(strings):
    if not isinstance(strings, list) or not all((isinstance(s, str) for s in strings)):
        raise ValueError('Input must be a list of strings.')
    first_letters = []
    for string in strings:
        if string:
            first_letters.append(string[0])
    return first_letters
if __name__ == '__main__':
    sample_strings = ['Hello', 'world', 'Python', 'programming']
    try:
        result = extract_first_letters(sample_strings)
        print(result)
    except ValueError as e:
        print(e)