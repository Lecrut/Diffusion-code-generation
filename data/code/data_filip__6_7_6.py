def replace_spaces(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world python"
    result = replace_spaces(sample_input)
    print(result)