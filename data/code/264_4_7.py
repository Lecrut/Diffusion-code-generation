def find_unique_words(text):
    return set(word.lower() for word in text.split())

if __name__ == '__main__':
    sample_text = "Hello world! Hello everyone."
    unique_words = find_unique_words(sample_text)
    print(unique_words)