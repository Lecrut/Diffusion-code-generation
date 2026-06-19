def join_with_delimiter(list_of_strings, delimiter):
    if not isinstance(list_of_strings, list):
        raise TypeError("The first argument must be a list.")
    if not all(isinstance(item, str) for item in list_of_strings):
        raise ValueError("All elements of the list must be strings.")
    if not isinstance(delimiter, str):
        raise TypeError("The delimiter must be a string.")
    
    result = ""
    for i, element in enumerate(list_of_strings):
        result += element
        if i < len(list_of_strings) - 1:
            result += delimiter
    return result

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    custom_delimiter = "; "
    try:
        result = join_with_delimiter(sample_list, custom_delimiter)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)