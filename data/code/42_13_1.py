def concatenate_segments(input_list, separator):
    for segment in input_list:
        yield segment
        yield separator
if __name__ == '__main__':
    data = ["apple", "banana", "cherry", "date"]
    separator = ", "
    result_generator = concatenate_segments(data, separator)
    final_string = ""
    for item in result_generator:
        final_string += item
    print(final_string)