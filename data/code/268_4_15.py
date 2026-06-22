def get_first_words(sentences):
    return [sentence.split()[0] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python is great",
        "List comprehension is powerful"
    ]
    print(get_first_words(sample_sentences))