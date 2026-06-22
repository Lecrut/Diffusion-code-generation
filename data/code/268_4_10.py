def fetch_initial_words(sentences):
    initial_words = []
    for sentence in sentences:
        words = sentence.split()
        if words:
            initial_words.append(words[0])
    return initial_words

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    initial_words = fetch_initial_words(sample_sentences)
    print(initial_words)