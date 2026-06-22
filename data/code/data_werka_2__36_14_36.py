def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Python is fun to learn"
    print(reverse_sentence(sample_sentence))