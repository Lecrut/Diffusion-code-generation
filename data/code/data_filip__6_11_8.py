def convert_spaces_to_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello world this is a test string"
    result = convert_spaces_to_underscores(sample_text)
    print(result)