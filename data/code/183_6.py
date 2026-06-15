def extract_names(input_string):
    return input_string.split(';')
if __name__ == '__main__':
    sample_input = "Alice;Bob;Charlie;David"
    result = extract_names(sample_input)
    print(result)