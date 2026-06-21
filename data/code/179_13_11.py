def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    test_string = "hello world this is a test"
    print(reverse_words(test_string))