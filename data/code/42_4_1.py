def concatenate_segments(string_iterable, separator):
    for segment in string_iterable:
        yield segment
        yield separator
if __name__ == '__main__':
    input_strings = ["apple", "banana", "cherry"]
    custom_separator = "---"
    result_generator = concatenate_segments(input_strings, custom_separator)
    concatenated_string = ""
    for item in result_generator:
        concatenated_string += item
    print(concatenated_string)