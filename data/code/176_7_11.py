def extract_unique_sorted_words(paragraph):
    words = paragraph.split()
    distinct_words = sorted(set(words))
    return distinct_words

if __name__ == '__main__':
    sample_paragraph = "The quick brown fox jumps over the lazy dog. The dog barked at the fox."
    result = extract_unique_sorted_words(sample_paragraph)
    print(result)