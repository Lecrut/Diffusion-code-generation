def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text = "Hello world this is a test string"
    print(count_words(sample_text))