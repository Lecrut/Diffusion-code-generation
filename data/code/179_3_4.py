def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    test_string = "The quick brown fox"
    print(reverse_words(test_string))