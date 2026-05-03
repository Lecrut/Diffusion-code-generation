def join_with_delimiter(list_of_strings, delimiter):
    return delimiter.join(list_of_strings)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    sample_delimiter = ", "
    result = join_with_delimiter(sample_list, sample_delimiter)
    print(result)