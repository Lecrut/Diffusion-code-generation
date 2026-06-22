def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    result = reverse_words(sample_sentence)
    print(result)