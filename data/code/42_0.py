def concatenate_strings(string_list, delimiter):
    return delimiter.join(string_list)
if __name__ == '__main__':
    input_strings = ["apple", "banana", "cherry", "date"]
    separator = ", "
    result = concatenate_strings(input_strings, separator)
    print(result)