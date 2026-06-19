def join_with_delimiter(list_of_strings, delimiter):
    result = ""
    for i, string in enumerate(list_of_strings):
        if i > 0:
            result += delimiter
        result += string
    return result

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    combined_string = join_with_delimiter(fruits, separator)
    print(combined_string)