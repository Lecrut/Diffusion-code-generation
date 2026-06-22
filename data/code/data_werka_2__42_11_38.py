def concatenate_segments(strings, separator):
    for string in strings:
        yield f"{separator}{string}"

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    separator = ","
    result_generator = concatenate_segments(sample_strings, separator)
    
    concatenated_result = "".join(result_generator)
    print(concatenated_result)