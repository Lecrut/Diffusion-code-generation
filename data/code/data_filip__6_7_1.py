def replace_spaces_with_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world"
    result = replace_spaces_with_underscores(sample_text)
    print(result)