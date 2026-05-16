def concatenate_strings(string_list, delimiter):
    result = delimiter.join(string_list)
    return result
if __name__ == '__main__':
    input_strings = ["apple", "banana", "cherry", "date"]
    separator = ", "
    final_string = concatenate_strings(input_strings, separator)
    print(final_string)