def find_unique_words(text):
    words = set()
    for word in text.split():
        words.add(word.lower())
    return words

if __name__ == '__main__':
    sample_text = "Hello world hello Python"
    unique_words = find_unique_words(sample_text)
    print(unique_words)