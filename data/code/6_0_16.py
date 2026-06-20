def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "Hello World Example"
    result = replace_spaces_with_underscores(sample_input)
    print(result)