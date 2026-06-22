def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(count_words(sample_text))