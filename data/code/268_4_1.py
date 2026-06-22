def get_first_words(sentences):
    return [sentence.split()[0] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    print(get_first_words(sample_sentences))