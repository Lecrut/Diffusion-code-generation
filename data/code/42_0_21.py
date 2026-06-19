def concatenate_strings(string_list, delimiter):
    result = ""
    for string in string_list:
        if result:
            result += delimiter
        result += string
    return result

if __name__ == '__main__':
    sample_strings = ["dog", "cat", "bird"]
    separator = "; "
    combined_string = concatenate_strings(sample_strings, separator)
    print(combined_string)