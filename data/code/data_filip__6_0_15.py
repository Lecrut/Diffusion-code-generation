def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = replace_spaces_with_underscores(sample_input)
    print(result)