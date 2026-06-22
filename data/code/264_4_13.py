def find_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return unique_words

if __name__ == '__main__':
    sample_text = "hello world hello Python programming"
    print(find_unique_words(sample_text))