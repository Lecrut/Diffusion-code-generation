def separate_string(input_string):
    separated_chars = []
    for char in input_string:
        separated_chars.append(char)
    return separated_chars
if __name__ == '__main__':
    sample_string = "HelloWorld"
    print("Original string:", sample_string)
    result = separate_string(sample_string)
    print("Separated characters:", result)