def convert_spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world foo bar"
    result = convert_spaces_to_underscores(sample_text)
    print(result)