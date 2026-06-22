def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Python from world Hello"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)