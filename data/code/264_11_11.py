def extract_distinct_words(sentences):
    words = set()
    for sentence in sentences:
        words.update(sentence.split())
    return sorted(words)

if __name__ == '__main__':
    sample_sentences = [
        "hello world",
        "world peace",
        "hello everyone"
    ]
    distinct_words = extract_distinct_words(sample_sentences)
    print(distinct_words)