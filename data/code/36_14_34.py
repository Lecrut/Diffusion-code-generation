def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    reversed_sentence = reverse_sentence(sample_sentence)
    print(reversed_sentence)