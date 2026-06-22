def concatenate_segments(strings, separator):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements of the input list must be strings.")
    if not isinstance(separator, str):
        raise ValueError("Separator must be a string.")
    
    for index, string in enumerate(strings):
        if index > 0:
            yield separator
        yield string

if __name__ == '__main__':
    SAMPLE_STRINGS = ["apple", "banana", "cherry"]
    CUSTOM_SEPARATOR = ","
    result_generator = concatenate_segments(SAMPLE_STRINGS, CUSTOM_SEPARATOR)
    concatenated_result = ''.join(result_generator)
    print(concatenated_result)