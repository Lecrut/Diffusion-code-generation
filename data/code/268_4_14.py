def fetch_first_word(sentence):
    return sentence.split()[0]

def process_sentences(sentences):
    words = []
    for sentence in sentences:
        first_word = fetch_first_word(sentence)
        words.append(first_word)
    return words

if __name__ == '__main__':
    sample_sentences = [
        "Good morning",
        "The quick brown fox jumps over the lazy dog",
        "Data structures and algorithms"
    ]
    result = process_sentences(sample_sentences)
    print(result)