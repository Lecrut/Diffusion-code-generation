def extract_distinct_words(text):
    words = text.lower().split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world hello Python programming is fun"
    print(extract_distinct_words(sample_text))