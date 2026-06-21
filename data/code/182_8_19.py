def separate_string(input_string):
    return [(i, char) for i, char in enumerate(input_string)]

if __name__ == '__main__':
    sample_string = "Hello World"
    result = separate_string(sample_string)
    print("Separated characters with indices:", result)