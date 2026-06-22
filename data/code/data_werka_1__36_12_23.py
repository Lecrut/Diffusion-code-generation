def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result = reverse_words(sample_input)
    print(result)