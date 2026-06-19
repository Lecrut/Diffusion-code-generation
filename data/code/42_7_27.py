def join_with_delimiter(list_of_strings, delimiter):
    if not list_of_strings:
        return ""
    return delimiter.join(list_of_strings)

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "date"]
    separator = "; "
    combined_string = join_with_delimiter(fruits, separator)
    print(combined_string)