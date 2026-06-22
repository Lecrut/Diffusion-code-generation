def join_strings_with_delimiter(strings, delimiter):
    return delimiter.join(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_delimiter = ", "
    result = join_strings_with_delimiter(sample_strings, custom_delimiter)
    print(result)