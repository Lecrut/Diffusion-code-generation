def replace_spaces_with_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World This Is A Test"
    result = replace_spaces_with_underscores(sample_input)
    print(result)