def concatenate_segments(strings, separator):
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements of the input list must be strings.")
    if not isinstance(separator, str):
        raise ValueError("Separator must be a string.")
    
    for i, string in enumerate(strings):
        if i > 0:
            yield separator
        yield string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = ", "
    result_generator = concatenate_segments(sample_strings, custom_separator)
    concatenated_result = ''.join(result_generator)
    print(concatenated_result)