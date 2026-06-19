def concatenate_segments(iterable, separator):
    SEPARATOR = separator
    for segment in iterable:
        yield segment
        yield SEPARATOR

if __name__ == '__main__':
    string_list = ["apple", "banana", "cherry"]
    separator_string = " - "
    result_generator = concatenate_segments(string_list, separator_string)
    final_result = ""
    for item in result_generator:
        final_result += item
    print(final_result.rstrip(separator_string))