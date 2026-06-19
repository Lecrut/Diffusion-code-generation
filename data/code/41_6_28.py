def convert_to_title_case(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list of strings")
    
    title_cased_strings = []
    for string in strings:
        if not isinstance(string, str):
            raise ValueError("All elements in the list must be strings")
        title_cased_strings.append(string.title())
    
    return title_cased_strings

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON programming", "this is a TEST"]
    try:
        title_cased_strings = convert_to_title_case(sample_strings)
        print(title_cased_strings)
    except ValueError as e:
        print(e)