def concatenate_strings(string_list, delimiter):
    if not string_list:
        return ""
    return delimiter.join(string_list)

if __name__ == '__main__':
    sample_strings = ["cat", "dog", "elephant"]
    separator = " - "
    combined_string = concatenate_strings(sample_strings, separator)
    print(combined_string)