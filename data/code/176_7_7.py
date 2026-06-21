def extract_unique_words(paragraph):
    words = paragraph.split()
    unique_words = sorted(set(words))
    return unique_words

if __name__ == '__main__':
    sample_text = "Hello world! Hello everyone. Welcome to the world of Python."
    unique_sorted_words = extract_unique_words(sample_text)
    print(unique_sorted_words)