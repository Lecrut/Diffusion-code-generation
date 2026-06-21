def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "Python is fun"
    result = reverse_words(test_string)
    print(result)