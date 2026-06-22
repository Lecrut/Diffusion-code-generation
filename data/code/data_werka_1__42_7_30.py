def join_with_delimiter(list_of_strings, delimiter):
    if not isinstance(list_of_strings, list) or not all(isinstance(s, str) for s in list_of_strings):
        raise ValueError("The first argument must be a list of strings.")
    if not isinstance(delimiter, str):
        raise ValueError("The second argument must be a string.")
    
    return delimiter.join(list_of_strings)

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    try:
        joined_string = join_with_delimiter(fruits, separator)
        print(joined_string)
    except ValueError as e:
        print(e)