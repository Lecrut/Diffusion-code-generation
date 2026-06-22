def find_words(text):
    words = text.split()
    return words

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(find_words(sample_text))