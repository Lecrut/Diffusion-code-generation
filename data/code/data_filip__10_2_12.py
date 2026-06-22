def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample1 = "Hello   World"
    sample2 = "  Python  is  great  "
    sample3 = "SingleWord"
    sample4 = ""
    sample5 = "   "
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))