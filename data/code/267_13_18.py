def filter_long_words(sentence):
    if not isinstance(sentence, str) or not sentence:
        raise ValueError("Invalid input: Input must be a non-empty string.")
    
    words = sentence.split()
    long_words = [word for word in words if len(word) > 3]
    return long_words

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    try:
        result = filter_long_words(sample_sentence)
        print(result)
    except ValueError as e:
        print(e)