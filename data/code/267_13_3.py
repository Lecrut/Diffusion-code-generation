def filter_long_words(sentence):
    if not isinstance(sentence, str) or not sentence:
        raise ValueError("Invalid input: Input must be a non-empty string.")
    
    return [word for word in sentence.split() if len(word) > 3]

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    try:
        long_words = filter_long_words(sample_sentence)
        print(long_words)
    except ValueError as e:
        print(e)