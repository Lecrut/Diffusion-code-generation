def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample = "Hello World"
    print(reverse_words(sample))