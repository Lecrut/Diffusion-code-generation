def extract_first_letters(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list.")
    first_letters = []
    for string in strings:
        if not isinstance(string, str):
            raise ValueError("All elements in the list must be strings.")
        if string:
            first_letters.append(string[0])
    return first_letters

if __name__ == '__main__':
    sample_strings = ['blueberry', 'cherry', 'dragonfruit', 'elderberry']
    try:
        result = extract_first_letters(sample_strings)
        print(result)
    except ValueError as e:
        print(e)