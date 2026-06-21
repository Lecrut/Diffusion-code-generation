def separate_string(input_string):
    return [(i, char) for i, char in enumerate(input_string)]

if __name__ == '__main__':
    sample_string = "Python Programming"
    print("Original string:", sample_string)
    result = separate_string(sample_string)
    print("Separated characters with indices:", result)