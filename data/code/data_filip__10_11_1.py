def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample = "  Hello   world!  This is   a test.  "
    print(reverse_words(sample))
    sample2 = "one"
    print(reverse_words(sample2))
    sample3 = "  "
    print(reverse_words(sample3))
    sample4 = "  leading   and   trailing  "
    print(reverse_words(sample4))