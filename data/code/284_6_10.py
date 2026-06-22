def reverse_words(sentence):
    words = sentence.split()
    if not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a string containing only words separated by spaces")
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)