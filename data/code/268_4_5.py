def validate_sentences(sentences):
    if not all(isinstance(sentence, str) for sentence in sentences):
        raise ValueError("All elements in the list must be strings")

def get_first_words(sentences):
    validate_sentences(sentences)
    return [sentence.split()[0] for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    print(get_first_words(sample_sentences))