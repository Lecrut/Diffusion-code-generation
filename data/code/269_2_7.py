def extract_word_punctuation_pairs(sentence):
    pairs = []
    words = sentence.split()
    for word in words:
        if len(word) > 1 and word[-2] in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            pairs.append((word[:-2], word[-2]))
        elif len(word) > 0 and word[-1] in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            pairs.append((word[:-1], word[-1]))
    return pairs

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you today? This is a test sentence; isn't it?"
    result = extract_word_punctuation_pairs(sample_sentence)
    print(result)