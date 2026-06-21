def tokenize(text):
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello\tWorld\nThis is a test"
    tokens = tokenize(sample_text)
    print(tokens)