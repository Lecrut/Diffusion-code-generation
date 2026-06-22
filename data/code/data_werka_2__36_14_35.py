def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    print(reverse_sentence(sample_sentence))