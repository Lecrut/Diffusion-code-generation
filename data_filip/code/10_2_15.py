def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

if __name__ == '__main__':
    sentence = "  Hello   world  "
    result = reverse_words(sentence)
    print(result)