def separate_string(input_string):
    separated_chars = []
    for char in input_string:
        separated_chars.append(char)
    return separated_chars
if __name__ == '__main__':
    sample_string = "Hello World"
    print("Original String:", sample_string)
    result = separate_string(sample_string)
    print("Separated Characters:", result)