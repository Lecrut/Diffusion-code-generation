def split_multiple_whitespaces(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello\tWorld\nThis is a test."
    tokens = split_multiple_whitespaces(sample_text)
    print(tokens)