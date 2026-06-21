def separate_characters(input_string):
    return '-'.join(char for char in input_string)

if __name__ == '__main__':
    sample_input = "hello"
    print(separate_characters(sample_input))