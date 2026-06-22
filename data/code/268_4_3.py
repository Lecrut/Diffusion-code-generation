def extract_first_words(sentences):
    words = []
    for sentence in sentences:
        parts = sentence.split()
        if parts:
            words.append(parts[0])
    return words

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    first_words = extract_first_words(sample_sentences)
    print(first_words)