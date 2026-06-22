def extract_distinct_words(sentences):
    words = set(word.lower() for sentence in sentences for word in sentence.split())
    return sorted(words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "The quick brown fox jumps over the lazy dog",
        "Hello Python"
    ]
    distinct_words = extract_distinct_words(sample_sentences)
    print(distinct_words)