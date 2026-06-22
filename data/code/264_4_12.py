def find_unique_words(text):
    words = set(word.lower() for word in text.split())
    return words

if __name__ == '__main__':
    sample_text = "Hello world hello Python"
    unique_words = find_unique_words(sample_text)
    print(unique_words)