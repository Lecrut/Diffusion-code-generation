def separate_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    separated_chars = [(i, char) for i, char in enumerate(input_string)]
    return separated_chars

if __name__ == '__main__':
    sample_string = "Hello World"
    print("Original string:", sample_string)
    result = separate_string(sample_string)
    print("Separated characters:", result)