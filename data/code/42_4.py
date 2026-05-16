def concatenate_segments(iterable, separator):
    for segment in iterable:
        yield segment
        yield separator
if __name__ == '__main__':
    string_list = ["apple", "banana", "cherry"]
    separator_string = " | "
    result_generator = concatenate_segments(string_list, separator_string)
    final_string = ""
    for item in result_generator:
        final_string += item
    print(final_string)