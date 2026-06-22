def validate_input(string_list, delimiter):
    if not isinstance(string_list, list) or not all(isinstance(s, str) for s in string_list):
        raise ValueError("string_list must be a list of strings")
    if not isinstance(delimiter, str):
        raise ValueError("delimiter must be a string")

def concatenate_strings(string_list, delimiter):
    validate_input(string_list, delimiter)
    return delimiter.join(string_list)

if __name__ == '__main__':
    sample_strings = ["red", "green", "blue"]
    separator = " | "
    result = concatenate_strings(sample_strings, separator)
    print(result)