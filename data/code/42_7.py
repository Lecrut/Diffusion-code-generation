def join_with_delimiter(list_of_strings, delimiter):
    return delimiter.join(list_of_strings)
if __name__ == '__main__':
    strings = ["apple", "banana", "cherry", "date"]
    delimiter = ", "
    result = join_with_delimiter(strings, delimiter)
    print(result)