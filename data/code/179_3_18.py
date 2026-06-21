def reverse_words(s):
    words = s.split()
    reversed_words = list(reversed(words))
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "Python is fun to learn"
    result = reverse_words(test_string)
    print(result)