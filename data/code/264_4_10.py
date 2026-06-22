def find_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return unique_words

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    print(find_unique_words(sample_text))