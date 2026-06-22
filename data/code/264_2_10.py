def extract_and_sort_words(text):
    words = set(word.lower() for word in text.split())
    return sorted(words)

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming"
    print(extract_and_sort_words(sample_text))