def concatenate_segments(iterable, separator):
    for segment in iterable:
        yield segment
        yield separator

if __name__ == '__main__':
    SAMPLE_STRINGS = ["apple", "banana", "cherry"]
    CUSTOM_SEPARATOR = " - "
    result_generator = concatenate_segments(SAMPLE_STRINGS, CUSTOM_SEPARATOR)
    concatenated_result = ''.join(result_generator).rstrip(CUSTOM_SEPARATOR)
    print(concatenated_result)