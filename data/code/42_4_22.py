def concatenate_with_separator(strings, separator):
    for string in strings:
        yield f"{separator}{string}"

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = "-"
    
    concatenated_segments = concatenate_with_separator(sample_strings, custom_separator)
    result = ''.join(concatenated_segments)
    print(result)