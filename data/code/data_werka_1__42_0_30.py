def concatenate_strings(string_list, delimiter):
    if not isinstance(string_list, list):
        raise ValueError("The first argument must be a list.")
    if not all(isinstance(item, str) for item in string_list):
        raise ValueError("All items in the list must be strings.")
    if not isinstance(delimiter, str):
        raise ValueError("The delimiter must be a string.")
    
    result = ""
    for index, string in enumerate(string_list):
        result += string
        if index < len(string_list) - 1:
            result += delimiter
    return result

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    separator = ", "
    try:
        combined_string = concatenate_strings(sample_strings, separator)
        print(combined_string)
    except ValueError as e:
        print(e)