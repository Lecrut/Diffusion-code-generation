def get_first_letters(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings")
    
    return [s[0] for s in strings if s and isinstance(s, str)]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date", "", 123]
    try:
        result = get_first_letters(sample_strings)
        print(result)
    except ValueError as e:
        print(e)