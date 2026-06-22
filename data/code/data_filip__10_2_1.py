def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample1 = "Hello   world"
    sample2 = "  Python  is  great  "
    sample3 = "One"
    sample4 = "   "
    print(reverse_words_in_sentence(sample1))
    print(reverse_words_in_sentence(sample2))
    print(reverse_words_in_sentence(sample3))
    print(reverse_words_in_sentence(sample4))