def concatenate_segments(strings, separator):
    for index, string in enumerate(strings):
        if index > 0:
            yield separator
        yield string

if __name__ == '__main__':
    sample_strings = ["cat", "dog", "bird"]
    custom_separator = ";"
    result_generator = concatenate_segments(sample_strings, custom_separator)
    concatenated_result = ''.join(result_generator)
    print(concatenated_result)