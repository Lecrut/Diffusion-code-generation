def join_with_delimiter(list_of_strings, delimiter):
    result = ""
    for i, string in enumerate(list_of_strings):
        if i > 0:
            result += delimiter
        result += string
    return result

if __name__ == '__main__':
    FRUIT_LIST = ["apple", "banana", "cherry", "date"]
    CUSTOM_DELIMITER = "; "
    JOINED_STRING = join_with_delimiter(FRUIT_LIST, CUSTOM_DELIMITER)
    print(JOINED_STRING)