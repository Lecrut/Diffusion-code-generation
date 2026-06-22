def filter_long_words(sentence):
    word_map = {word: len(word) for word in sentence.split()}
    long_words = [word for word, length in word_map.items() if length > 3]
    return long_words

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    result = filter_long_words(sample_sentence)
    print(result)