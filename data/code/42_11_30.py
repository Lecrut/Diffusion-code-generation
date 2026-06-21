def concatenate_segments(strings, separator):
    for string in strings:
        yield string + separator

DEFAULT_SEPARATOR = ","

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    result_generator = concatenate_segments(sample_strings, DEFAULT_SEPARATOR)
    concatenated_result = ''.join(result_generator).rstrip(DEFAULT_SEPARATOR)
    print(concatenated_result)