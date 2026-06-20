def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    test_cases = [
        "  Hello   World  ",
        "This   is  a test",
        "  leading and trailing  ",
        "single",
        "   "
    ]
    for case in test_cases:
        print(reverse_words(case))