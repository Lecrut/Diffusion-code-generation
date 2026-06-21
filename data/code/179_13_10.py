def reverse_words(sentence):
    words = sentence.split()
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the input must be strings")
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_words(sample_sentence))