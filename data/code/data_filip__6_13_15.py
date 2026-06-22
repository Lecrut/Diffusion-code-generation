def replace_spaces_with_underscore(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World Example String"
    result = replace_spaces_with_underscore(sample_input)
    print(result)