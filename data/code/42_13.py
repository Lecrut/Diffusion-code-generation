def concatenate_segments(input_list, separator):
    for segment in input_list:
        yield segment
        yield separator
if __name__ == '__main__':
    data = ["apple", "banana", "cherry", "date"]
    separator = ", "
    result_generator = concatenate_segments(data, separator)
    concatenated_string = ""
    for item in result_generator:
        concatenated_string += item
    print(concatenated_string)