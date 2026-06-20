def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample = "Hello world from Python"
    result = reverse_words(sample)
    print(result)