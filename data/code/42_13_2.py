def concatenate_segments(input_list, separator):
    for segment in input_list:
        yield segment
        yield separator
if __name__ == '__main__':
    data = ["apple", "banana", "cherry", "date"]
    separator = ", "
    generator = concatenate_segments(data, separator)
    result = "".join(generator)
    print(result)