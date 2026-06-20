def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello World from Python"
    result = reverse_words(sample_sentence)
    print(result)