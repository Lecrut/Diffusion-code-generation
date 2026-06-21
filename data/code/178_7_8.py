def split_multiple_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello\tWorld\nThis is a test"
    print(split_multiple_whitespace(sample_text))