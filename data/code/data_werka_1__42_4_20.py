def concatenate_with_separator(strings, separator):
    for string in strings:
        yield f"{separator}{string}"

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    custom_separator = "-"
    result_generator = concatenate_with_separator(sample_strings, custom_separator)
    
    for item in result_generator:
        print(item)