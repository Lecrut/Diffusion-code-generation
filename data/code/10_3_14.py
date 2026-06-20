def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word for word in reversed(words)]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello World from Python"
    result = reverse_words(sample_sentence)
    print(result)