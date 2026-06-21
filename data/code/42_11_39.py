def concatenate_segments(strings, separator):
    for string in strings:
        yield f"{string}{separator}" if string else ""

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = ","
    result_generator = concatenate_segments(sample_strings, custom_separator)
    concatenated_result = ''.join(result_generator).rstrip(custom_separator)
    print(concatenated_result)