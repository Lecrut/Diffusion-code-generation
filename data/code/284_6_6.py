def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)