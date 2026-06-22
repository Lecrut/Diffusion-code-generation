def concatenate_segments(strings, separator):
    for string in strings:
        yield string + separator

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    separator = ","
    result_generator = concatenate_segments(sample_strings, separator)
    
    for segment in result_generator:
        print(segment, end='')