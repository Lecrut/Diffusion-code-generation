def extract_sorted_words(text):
    words = set(word.lower() for word in text.split())
    return sorted(words)

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming"
    print(extract_sorted_words(sample_text))