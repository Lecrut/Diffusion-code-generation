THRESHOLD = 3

def filter_long_words(sentence):
    return [word for word in sentence.split() if len(word) > THRESHOLD]

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    long_words = filter_long_words(sample_sentence)
    print(long_words)