def reverse_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample_sentence = "Efficient implementation of Python function"
    print(reverse_sentence(sample_sentence))