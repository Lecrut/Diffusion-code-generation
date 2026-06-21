def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    TEST_STRING = "The quick brown fox"
    print(reverse_words(TEST_STRING))