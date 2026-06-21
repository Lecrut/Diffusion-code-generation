def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return reversed_words

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    result = reverse_sentence(sample_sentence)
    print(result)