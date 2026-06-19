def validate_input(string_list, delimiter):
    if not isinstance(string_list, list):
        raise ValueError("The first argument must be a list of strings.")
    if not all(isinstance(s, str) for s in string_list):
        raise ValueError("All elements in the list must be strings.")
    if not isinstance(delimiter, str):
        raise ValueError("The delimiter must be a string.")

def concatenate_strings(string_list, delimiter):
    validate_input(string_list, delimiter)
    return delimiter.join(string_list)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    separator = " - "
    result = concatenate_strings(sample_strings, separator)
    print(result)