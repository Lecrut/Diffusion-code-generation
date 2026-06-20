def replace_whitespace_with_underscores(text):
    return ''.join('_' if char.isspace() else char for char in text)

if __name__ == '__main__':
    sample_text = "Hello World!   How are you?"
    result = replace_whitespace_with_underscores(sample_text)
    print(result)