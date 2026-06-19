def concatenate_strings(string_list, delimiter):
    concatenated_result = ""
    for index, string in enumerate(string_list):
        if index > 0:
            concatenated_result += delimiter
        concatenated_result += string
    return concatenated_result

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    separator = " - "
    final_output = concatenate_strings(sample_strings, separator)
    print(final_output)