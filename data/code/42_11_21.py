def concatenate_segments(strings, separator):
    for string in strings:
        yield f"{separator}{string}" if separator else string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = ", "
    result_generator = concatenate_segments(sample_strings, custom_separator)
    
    concatenated_result = ''.join(result_generator)
    print(concatenated_result)