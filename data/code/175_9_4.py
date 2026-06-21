def reverse_sentence(sentence):
    words = sentence.split()
    return words[::-1]

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_words = reverse_sentence(sample_sentence)
    print(reversed_words)