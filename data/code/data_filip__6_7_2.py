def replace_spaces(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world python"
    result = replace_spaces(sample_text)
    print(result)