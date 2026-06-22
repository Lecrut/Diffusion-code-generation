def extract_first_word(sentence):
    parts = sentence.split()
    if not parts:
        raise ValueError("Sentence is empty")
    return parts[0]

def get_first_words(sentences):
    return [extract_first_word(sentence) for sentence in sentences]

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    first_words = get_first_words(sample_sentences)
    print(first_words)