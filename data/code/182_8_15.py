def separate_string_with_indices(input_string):
    return [(index, char) for index, char in enumerate(input_string)]

if __name__ == '__main__':
    sample_string = "Hello World"
    print("Original string:", sample_string)
    result = separate_string_with_indices(sample_string)
    print("Separated characters with indices:", result)