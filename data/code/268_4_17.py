MAX_SENTENCE_LENGTH = 1024

def extract_first_word(sentence):
    return sentence.split()[0] if len(sentence) <= MAX_SENTENCE_LENGTH else None

if __name__ == '__main__':
    sample_sentences = [
        "Hello world",
        "Python programming is fun",
        "List comprehension in Python"
    ]
    first_words = [extract_first_word(sentence) for sentence in sample_sentences]
    print(first_words)