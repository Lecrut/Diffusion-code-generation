def count_words(text):
    words = text.lower().split()
    return len(words)

if __name__ == '__main__':
    sample_text = "Hello World! This is a test."
    print(count_words(sample_text))