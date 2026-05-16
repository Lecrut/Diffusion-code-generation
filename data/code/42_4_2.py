def concatenate_with_separator(string_iterable, separator):
    result = ""
    for s in string_iterable:
        result += s + separator
    yield result.rstrip(separator)
if __name__ == '__main__':
    input_strings = ["apple", "banana", "cherry"]
    separator_string = ", "
    generator = concatenate_with_separator(input_strings, separator_string)
    output_list = list(generator)
    print(output_list)