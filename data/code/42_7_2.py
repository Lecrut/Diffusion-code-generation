def join_with_delimiter(list_of_strings, delimiter):
    return delimiter.join(list_of_strings)
if __name__ == '__main__':
    input_list = ["apple", "banana", "cherry", "date"]
    custom_delimiter = " | "
    result = join_with_delimiter(input_list, custom_delimiter)
    print(result)