def reverse_words(s):
    return ' '.join(s.split()[::-1])
if __name__ == '__main__':
    test_string = "hello world this is a test"
    print(reverse_words(test_string))