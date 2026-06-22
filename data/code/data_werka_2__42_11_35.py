def concatenate_segments(strings, separator):
    for string in strings:
        yield f"{string}{separator}"

if __name__ == '__main__':
    sample_strings = ["dog", "cat", "bird"]
    custom_separator = ";"
    result_generator = concatenate_segments(sample_strings, custom_separator)
    concatenated_result = ''.join(result_generator).rstrip(custom_separator)
    print(concatenated_result)