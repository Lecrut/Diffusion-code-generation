def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    result = reverse_words(sample_sentence)
    print(result)