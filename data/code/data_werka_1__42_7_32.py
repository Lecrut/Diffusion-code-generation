def is_valid_list_of_strings(list_of_strings):
    return isinstance(list_of_strings, list) and all(isinstance(item, str) for item in list_of_strings)

def is_valid_delimiter(delimiter):
    return isinstance(delimiter, str)

def join_with_delimiter(list_of_strings, delimiter):
    if not is_valid_list_of_strings(list_of_strings):
        raise ValueError("The first argument must be a list of strings.")
    if not is_valid_delimiter(delimiter):
        raise ValueError("The second argument must be a string delimiter.")
    
    result = ""
    for i, string in enumerate(list_of_strings):
        result += string
        if i < len(list_of_strings) - 1:
            result += delimiter
    return result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    custom_delimiter = "; "
    try:
        result = join_with_delimiter(sample_list, custom_delimiter)
        print(result)
    except ValueError as e:
        print(e)