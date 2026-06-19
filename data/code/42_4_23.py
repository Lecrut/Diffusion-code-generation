def concatenate_segments(strings, separator):
    for string in strings:
        yield f"{separator}{string}"

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = "-"
    
    concatenated_result = ''.join(concatenate_segments(sample_strings, custom_separator))
    print(concatenated_result)